#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>

typedef struct matrix {
  double **data_;
  Py_ssize_t size_;
} matrix_t;

matrix_t create_empty_matrix(Py_ssize_t n) {
  matrix_t mat;
  mat.data_ = (double **)calloc(n, sizeof(double *));
  mat.size_ = n;

  for (Py_ssize_t i = 0; i < n; i++)
    mat.data_[i] = (double *)calloc(n, sizeof(double));

  return mat;
}

matrix_t create_identity_matrix(Py_ssize_t n) {
  matrix_t mat = create_empty_matrix(n);
  for (Py_ssize_t i = 0; i < n; i++)
    mat.data_[i][i] = 1;
  return mat;
}

void delete_mat(matrix_t *mat) {
  Py_ssize_t n = mat->size_;
  for (Py_ssize_t i = 0; i < n; i++)
    free(mat->data_[i]);
  free(mat->data_);
}

void multiply_matrix(matrix_t *A, matrix_t *B, matrix_t *res) {
  Py_ssize_t n = A->size_;
  for (Py_ssize_t i = 0; i < n; ++i) {
    for (Py_ssize_t j = 0; j < n; ++j) {
      res->data_[i][j] = 0.0;
      for (Py_ssize_t k = 0; k < n; ++k) {
        res->data_[i][j] += A->data_[i][k] * B->data_[k][j];
      }
    }
  }
}

matrix_t matrix_power(matrix_t *mat, Py_ssize_t pow) {
  matrix_t res;
  Py_ssize_t n = mat->size_;
  res = create_identity_matrix(n);
  for (Py_ssize_t h = 0; h < pow; h++) {
    matrix_t tmp_mat = create_empty_matrix(n);
    multiply_matrix(&res, mat, &tmp_mat);
    delete_mat(&res);
    res = tmp_mat;
  }
  return res;
}

int list_to_mat(PyObject *obj, void *ptr) {
  matrix_t *mat = ptr;
  Py_ssize_t n = PyList_Size(obj);

  *mat = create_empty_matrix(n);
  for (Py_ssize_t i = 0; i < n; i++) {
    PyObject *row = PyList_GetItem(obj, i);
    for (Py_ssize_t j = 0; j < n; j++)
      mat->data_[i][j] = PyFloat_AsDouble(PyList_GetItem(row, j));
  }

  return 1;
}

PyObject *mat_to_list(matrix_t *mat) {
  Py_ssize_t n = mat->size_;
  PyObject *py_mat = PyList_New(n);
  for (Py_ssize_t i = 0; i < n; i++) {
    PyObject *row = PyList_New(n);
    for (Py_ssize_t j = 0; j < n; j++)
      PyList_SetItem(row, j, PyFloat_FromDouble(mat->data_[i][j]));
    PyList_SetItem(py_mat, i, row);
  }

  return py_mat;
}

PyObject *foreign_matrix_power(PyObject *self, PyObject *args) {
  matrix_t mat;
  Py_ssize_t pow;

  if (!PyArg_ParseTuple(args, "O&n", list_to_mat, &mat, &pow))
    return NULL;

  matrix_t res = matrix_power(&mat, pow);
  PyObject *res_obj = mat_to_list(&res);

  delete_mat(&mat);
  delete_mat(&res);

  return res_obj;
}

static PyMethodDef ForeignMethods[] = {
    {"foreign_matrix_power", foreign_matrix_power, METH_VARARGS,
     "Fast powering of matrix"},
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef foreignmodule = {PyModuleDef_HEAD_INIT, "foreign",
                                           NULL, -1, ForeignMethods};

PyMODINIT_FUNC PyInit_foreign(void) { return PyModule_Create(&foreignmodule); };