#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t len = PyList_Size(p);
    PyObject *item;
    PyTypeObject *type;
    const char *type_name;
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", len);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < len; i++) {
        item = PyList_GetItem(p, i);
        type = Py_TYPE(item);
        type_name = type->tp_name;
        printf("Element %ld: %s\n", i, type_name);
        if (strcmp(type_name, "bytes") == 0) {
            print_python_bytes(item);
        }
    }
}

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t len = PyBytes_Size(p);
    char *str = PyBytes_AsString(p);
    Py_ssize_t i;

    printf("[.] bytes object info\n");
    if (PyBytes_Check(p)) {
        printf("  size: %ld\n", len);
        printf("  trying string: %s\n", str);
        printf("  first %ld bytes: ", len <= 10 ? len : 10);
        for (i = 0; i < len && i < 10; i++) {
            printf("%02hhx", str[i]);
            if (i < len - 1 && i < 9) {
                printf(" ");
            }
        }
        printf("\n");
    } else {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}
