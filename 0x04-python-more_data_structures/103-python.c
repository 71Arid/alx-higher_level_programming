#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t len, i;
    PyObject *item;
    const char *type_name;

    if (!PyList_Check(p)) {
        printf("Invalid List Object\n");
        return;
    }

    len = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", len);
    printf("[*] Allocated = %zd\n", ((PyListObject *) p)->allocated);

    for (i = 0; i < len; i++) {
        item = PyList_GetItem(p, i);
        type_name = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type_name);
        if (PyBytes_Check(item)) {
            printf("  [ERROR] Invalid Bytes Object\n");
        }
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *buffer;
    PyObject *bytes;
    const char *hex_digits = "0123456789abcdef";

    if (!PyBytes_Check(p)) {
        printf("Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", PyBytes_Size(p));

    bytes = PyBytes_FromStringAndSize(NULL, PyBytes_Size(p));
    if (!bytes) {
        printf("  [ERROR] Memory allocation failed\n");
        return;
    }

    size = PyBytes_AsStringAndSize(bytes, &buffer);
    if (size < 0) {
        printf("  [ERROR] Conversion to bytes failed\n");
        Py_DECREF(bytes);
        return;
    }

    printf("  trying string: %s\n", buffer);

    printf("  first %zd bytes: ", size < 10 ? size : 10);
    for (i = 0; i < (size < 10 ? size : 10); i++) {
        printf("%c%c", hex_digits[(unsigned char) buffer[i] >> 4], hex_digits[(unsigned char) buffer[i] & 15]);
        if (i < 9) {
            printf(" ");
        }
    }
    printf("\n");

    Py_DECREF(bytes);
}
