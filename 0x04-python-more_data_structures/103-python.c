#include <Python.h>
#include <stdio.h>

void print_hexn(const char *str, int n)
{
	int i = 0;

	for (; i < n - 1; ++i)
		printf("%02x ", (unsigned char) str[i]);

	printf("%02x", str[i]);
}

void print_python_bytes(PyObject *py_object)
{
	PyBytesObject *bytes_obj = (PyBytesObject *) py_object;
	int calc_bytes, obj_size = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(bytes_obj))
	{
		obj_size = PyBytes_Size(py_object);
		calc_bytes = obj_size + 1;

		if (calc_bytes >= 10)
			calc_bytes = 10;

		printf("  size: %d\n", obj_size);
		printf("  trying string: %s\n", bytes_obj->ob_sval);
		printf("  first %d bytes: ", calc_bytes);
		print_hexn(bytes_obj->ob_sval, calc_bytes);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

void print_python_list(PyObject *py_object)
{
	int i = 0, list_len = 0;
	PyObject *item;
	PyListObject *list_obj = (PyListObject *) py_object;

	printf("[*] Python list info\n");
	list_len = PyList_GET_SIZE(py_object);
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int) list_obj->allocated);

	for (; i < list_len; ++i)
	{
		item = PyList_GET_ITEM(py_object, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
