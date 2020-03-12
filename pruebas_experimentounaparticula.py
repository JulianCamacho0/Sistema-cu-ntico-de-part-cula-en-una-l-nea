
import unittest
import cnyt_unaparticula as cn

class TestStringMethods(unittest.TestCase):

    def test_probabilidad_particula_estado_x(self):

        v_one = [[2,1],[-1,2],[0,1],[1,0],[3,-1],[2,0],[0,-2],[-2,1],[1,-3],[0,-1]]

        self.assertEqual(cn.probabilidad_particula_estado_x(v_one,7), 10.87)

    def test_AmplitudTransicion(self):

        v_one = [[2,1],[-1,2],[0,1],[1,0],[3,-1],[2,0],[0,-2],[-2,1],[1,-3],[0,-1]]
        v_two = [[-1,-4],[2,-3],[-7,6],[-1,1],[-5,-3],[5,0],[5,8],[4,-4],[8,-7],[2,-7]]

        self.assertEqual(cn.AmplitudTransicion(v_one, v_two),[-0.021, -0.13])

if __name__ == '__main__':
     
    unittest.main()

