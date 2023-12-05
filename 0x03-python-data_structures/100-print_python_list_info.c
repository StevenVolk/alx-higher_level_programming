#include <stdio.h>
#include "/usr/include/python3.8/Python.h"

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: python list
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *python_list = (PyListObject *) p;
	int i, list_length = Py_SIZE(p);
	PyObject *element;

	printf("[*] Size of the Python List = %d\n", list_length);
	printf("[*] Allocated = %d\n", (int) python_list->allocated);

	for (i = 0; i < list_length; i++)
	{
		element = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, element->ob_type->tp_name);
	}
}
