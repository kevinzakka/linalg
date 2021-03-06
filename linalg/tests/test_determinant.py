import unittest
import numpy as np
import numpy.linalg as LA

from linalg import determinant, determinant_abs


class DeterminantTest(unittest.TestCase):
  """Tests the determinant of a square matrix A.
  """
  def test_no_log(self):
    T = np.array([
      [2, 1, 1, 0],
      [4, 3, 3, 1],
      [8, 7, 9, 5],
      [6, 7, 9, 8]
    ])

    actual = determinant(T)
    expected = LA.det(T)

    self.assertTrue(np.allclose(actual, expected))

  def test_log(self):
    T = np.eye(100) * 0.1

    actual = determinant(T, log=True)
    expected = LA.slogdet(T)

    self.assertTrue(all(np.allclose(a, e) for a, e in zip(actual, expected)))

  def test_det_abs(self):
    T = np.array([
      [2, 1, 1, 0],
      [4, 3, 3, 1],
      [8, 7, 9, 5],
      [6, 7, 9, 8]
    ])

    actual = np.abs(determinant_abs(T))
    expected = np.abs(LA.det(T))

    self.assertTrue(np.allclose(actual, expected))


if __name__ == '__main__':
  unittest.main()