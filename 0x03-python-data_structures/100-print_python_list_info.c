#include <Python.h>

/**
 * print_python_list_info - Print information about a Python list object.
 * @p: Pointer to a Python list object (PyObject).
 *
 * This function prints information about a Python list, including its size,
 * allocated memory, and the types of elements in the list.
 */

void print_python_list_info(PyObject *p)
{
	int memory, size, i;
	PyObject *pobj;

	memory = ((PyListObject *)(p))->allocated;
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", memory);
	for (i = 0 ; i < size ; i++)
	{
		pobj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(pobj)->tp_name);
	}
}
