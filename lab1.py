import sys
import numpy as np
import matplotlib.pyplot as plt


class Func:

    def __init__(self, x: list, theta: list, a: list, c: int):
        '''

        :param x: a two-dimensional list RxN, where each nested list is the coordinates of one point
        :param theta: a matrix of parameters RxR
        :param a: parameter vector Rx1
        :param c: scalar
        '''
        self.x = np.array(x).transpose()
        self.theta = np.array(theta)
        self.a = np.array(a).reshape(-1, 1)
        self.c = c

    def quadratic(self):
        self.f = np.zeros(self.x.shape[1])
        for i in range(np.size(self.x, 2)):
            self.pp = self.x[:, i]
            ans = np.dot(np.dot(self.pp.T, self.theta), self.pp) + np.dot(self.pp.T, self.a) + self.c
            self.f[i] = ans
        return self.f

    def lab_one_quadratic(self):

        # Вычисление значений целевой функции
        f = self.quadratic()

        # Превращение f из вектора-строки в двумерный массив
        f = f.reshape(cx.shape)

        # Построение графиков
        plt.figure(figsize=(12, 9))

        plt.subplot(2, 2, 1)
        plt.title("Surface Plot")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.plot_surface(cx, cy, f, cmap="viridis")

        plt.subplot(2, 2, 2)
        plt.title("Mesh Plot")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.plot_wireframe(cx, cy, f, cmap="viridis")

        plt.subplot(2, 2, 3)
        plt.title("Contour Plot")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.contour(cx, cy, f, cmap="viridis")

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
    # # TODO: ввод должен быть по столбцам, а не строкам
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
    # c = int(input('c: '))

    # Пределы и шаг изменения координат
    x_limits = np.arange(-1, 1.05, 0.05)
    y_limits = np.arange(-1, 1.05, 0.05)

    # Создание координатной сетки
    cx, cy = np.meshgrid(x_limits, y_limits)

    # Объединение cx и cy в единый массив
    xy = np.vstack((cx.ravel(), cy.ravel()))
    x = list(xy)
    print(x)
    # Задание параметров квадратичной функции
    theta = [[3, 1], [1, 2]]
    a = [0, 0]
    c = 1



    f = Func(x, theta, a, c)
    # print(x)
    # print(theta)
    # print(a)
    # print(c)


if __name__ == "__main__":
    main()