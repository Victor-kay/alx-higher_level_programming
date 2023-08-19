#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes object information
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p) {
    long int size, i;
    unsigned char *bytes;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = (unsigned char *)PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %ld bytes:", size > 10 ? 10 : size);
    for (i = 0; i < (size > 10 ? 10 : size); i++) {
        printf(" %02x", bytes[i]);
    }
    printf("\n");
}

/**
 * print_python_list - Prints list object information
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p) {
    long int size, i;
    PyObject *item;

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}
