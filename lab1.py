import sys

import numpy as np
import matplotlib.pyplot as plt


class Func:

    def __init__(self, theta, a, c):

        self.theta = theta
        self.a = a.reshape(-1, 1)

        self.x0 = self._calc_min()
        self.c = c

        self.cx, self.cy = self._get_mashgrid()
        self.xy = np.vstack((self.cx.ravel(), self.cy.ravel()))

    def _calc_min(self):
        # Расчет точки минимума
        return -np.linalg.inv(2 * self.theta) @ self.a

    def _get_mashgrid(self):
        # Пределы и шаг изменения координат
        x_limits = np.arange(self.x0[0][0]-1, self.x0[0][0]+1.05, 0.05)
        y_limits = np.arange(self.x0[1][0]-1, self.x0[1][0]+1.05, 0.05)
        # Создание координатной сетки
        return np.meshgrid(x_limits, y_limits)

    def quadratic(self):
        f = np.zeros(self.xy.shape[1])
        size = np.size(self.xy, 1)
        for i in range(size):
            pp = self.xy[:, i]
            f[i] = np.dot(np.dot(pp.T, self.theta), pp) + np.dot(pp.T, self.a) + self.c
        return f



    def lab_one_quadratic(self, f):
        f = f.reshape(self.cx.shape)

        fig = plt.figure(figsize=(12, 9))

        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_title("Mesh Plot")
        ax1.plot_wireframe(self.cx, self.cy, f, cmap="viridis")

        ax2 = fig.add_subplot(122)
        ax2.set_title("Contour Plot")
        contour = ax2.contour(self.cx, self.cy, f, cmap="viridis", levels=10)
        plt.clabel(contour, inline=True, fontsize=10)
        plt.colorbar(contour)

        ax2.set_aspect("equal")

        # ax2.axis("tight")
        # ax2.autoscale(enable=True, axis='y', tight=True)
        # plt.tight_layout()
        # plt.show()

        L, V = np.linalg.eig(self.theta)
        # Извлечение главной диагонали не требуется, возвращает массив
        # L = np.diag(L)

        # Вывод собственных значений и коэффициента обусловленности
        print('Собственные значения:')
        print(L)
        cond_number = np.max(L) / np.min(L)
        print('Коэффициент обусловленности:', cond_number)

        # Расчет точки минимума
        x0 = -np.linalg.inv(2 * self.theta) @ self.a
        # Построение собственных векторов в виде отрезков, выходящих из точки x0
        for i in range(len(L)):
            vect = V[:, i]
            ax2.plot([x0[0], x0[0] + vect[0]], [x0[1], x0[1] + vect[1]])

        plt.tight_layout()
        plt.show()


def str_to_int_list(st: str) -> list[int]:
    st = st.strip().replace(' ', '').split(',')
    try:
        st = [int(x) for x in st]
    except ValueError as e:
        print(f'{e.args[0]}\ntry again...')
        sys.exit()
    return st


def main():
    # R = int(input("enter R: "))
    # N = int(input("enter N: "))
    #
    # x = []
    # TODO: переделать ввод со списков на ndarray
    # for elem in range(N):
    #     col = input(f'coords for {elem+1} point ({R} nums) sep-ed with ",": ')
    #     col = str_to_int_list(col)
    #     x.append(col)
    #
    # theta = []
    # for elem in range(R):
    #     row = input(f'theta params on {elem+1} row ({R} nums): ')
    #     row = str_to_int_list(row)
    #     theta.append(row)
    #
    # a = input(f'params for a ({R} nums): ')
    # a = str_to_int_list(a)
    # TODO: заменить int на дробное во всех преобраз.
    # c = float(input('c: '))


    theta_vars = [
        [[3, 1], [1, 2]],
        [[1, 0], [0, 1]],
        [[3, 0], [0, 1]],
        [[4, 1], [1, 2]],
        [[2, 1], [1, 3]],
        [[15, 3], [3, 1]]
    ]

    a_vars = [
        [0, 0],
        [0, 0],
        [2, 3],
        [0, 0],
        [3, -1],
        [-1, 2]
    ]


    # # Пределы и шаг изменения координат
    # x_limits = np.arange(-1, 1.05, 0.05)
    # y_limits = np.arange(-1, 1.05, 0.05)
    #
    # # Создание координатной сетки
    # cx, cy = np.meshgrid(x_limits, y_limits)
    # Объединение cx и cy в единый массив

    # Задание параметров квадратичной функции
    for i in range(len(theta_vars)):
        theta = np.array(theta_vars[i])
        a = np.array(a_vars[i])
        c = 1

        func = Func(theta, a, c)
        f_answ = func.quadratic()
        func.lab_one_quadratic(f_answ)



if __name__ == "__main__":
    main()

