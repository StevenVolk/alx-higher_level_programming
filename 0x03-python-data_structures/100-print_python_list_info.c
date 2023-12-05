#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: python list
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *python_list = (PyListObject *)p;
	size_t i, list_length = PyList_Size(p);
	const char *element = NULL;

	printf("[*] Size of the Python List = %ld\n", list_length);
	printf("[*] Allocated = %ld\n", (signed long)(python_list->allocated));

	for (i = 0; i < list_length; i++)
	{
		element = Py_TYPE(py_list->ob_item[i])->tp_name;
		printf("Element %d: %s\n", i, py_type);
	}
}
