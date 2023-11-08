import unittest
from typing import Literal

from src.get_function_calling_schema import (
    FunctionDescriptionError,
    get_function_calling_schema,
    DESCRIPTION_SEPARATOR,
)


class TestFunctionCallingSchema(unittest.TestCase):
    def test_function_with_no_description(self):
        def func():
            pass

        with self.assertRaises(FunctionDescriptionError):
            get_function_calling_schema(func)

        with self.assertRaises(FunctionDescriptionError):
            get_function_calling_schema(func, include_long_description=True)

    def test_function_with_short_description(self):
        def func():
            """
            Short description.
            """
            pass

        expected_function_calling_schema = {
            "name": "func",
            "description": "Short description.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        }

        function_calling_schema = get_function_calling_schema(func)
        self.assertEqual(
            function_calling_schema,
            expected_function_calling_schema,
        )

        with self.assertRaises(FunctionDescriptionError):
            get_function_calling_schema(func, include_long_description=True)

    def test_function_with_long_description(self):
        def func():
            """
            Short description.

            Long description.
            """
            pass

        expected_function_calling_schema = {
            "name": "func",
            "description": "Short description.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        }
        function_calling_schema = get_function_calling_schema(
            func,
            include_long_description=False,
        )
        self.assertEqual(
            function_calling_schema,
            expected_function_calling_schema,
        )

        expected_function_calling_schema = {
            "name": "func",
            "description": DESCRIPTION_SEPARATOR.join(
                ["Short description.", "Long description."]
            ),
            "parameters": {"type": "object", "properties": {}, "required": []},
        }
        function_calling_schema = get_function_calling_schema(
            func,
            include_long_description=True,
        )
        self.assertEqual(
            function_calling_schema,
            expected_function_calling_schema,
        )

    def test_function_with_int_parameter(self):
        def func_with_rest_style_docstring(i):
            """
            Short description.

            :param i: Integer parameter.
            :type i: int
            """
            pass

        def func_with_google_style_docstring(i):
            """
            Short description.

            Args:
                i (int): Integer parameter.
            """
            pass

        def func_with_numpy_style_docstring(i):
            """
            Short description.

            Parameters
            ----------
            i : int
                Integer parameter.
            """
            pass

        def func_with_rest_style_docstring_type_hinted(i: int):
            """
            Short description.

            :param i: Integer parameter.
            """
            pass

        def func_with_google_style_docstring_type_hinted(i: int):
            """
            Short description.

            Args:
                i: Integer parameter.
            """
            pass

        def func_with_numpy_style_docstring_type_hinted(i: int):
            """
            Short description.

            Parameters
            ----------
            i :
                Integer parameter.
            """
            pass

        for func in [
            func_with_rest_style_docstring,
            func_with_google_style_docstring,
            func_with_numpy_style_docstring,
            func_with_rest_style_docstring_type_hinted,
            func_with_google_style_docstring_type_hinted,
            func_with_numpy_style_docstring_type_hinted,
        ]:
            expected_function_calling_schema = {
                "name": func.__name__,
                "description": "Short description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "i": {
                            "type": "number",
                            "description": "Integer parameter.",
                        }
                    },
                    "required": ["i"],
                },
            }
            function_calling_schema = get_function_calling_schema(func)
            self.assertEqual(
                function_calling_schema,
                expected_function_calling_schema,
            )

    def test_function_with_float_parameter(self):
        def func_with_rest_style_docstring(f):
            """
            Short description.

            :param f: Float parameter.
            :type f: float
            """
            pass

        def func_with_google_style_docstring(f):
            """
            Short description.

            Args:
                f (float): Float parameter.
            """
            pass

        def func_with_numpy_style_docstring(f):
            """
            Short description.

            Parameters
            ----------
            f : float
                Float parameter.
            """
            pass

        def func_with_rest_style_docstring_type_hinted(f: float):
            """
            Short description.

            :param f: Float parameter.
            """
            pass

        def func_with_google_style_docstring_type_hinted(f: float):
            """
            Short description.

            Args:
                f: Float parameter.
            """
            pass

        def func_with_numpy_style_docstring_type_hinted(f: float):
            """
            Short description.

            Parameters
            ----------
            f :
                Float parameter.
            """
            pass

        for func in [
            func_with_rest_style_docstring,
            func_with_google_style_docstring,
            func_with_numpy_style_docstring,
            func_with_rest_style_docstring_type_hinted,
            func_with_google_style_docstring_type_hinted,
            func_with_numpy_style_docstring_type_hinted,
        ]:
            expected_function_calling_schema = {
                "name": func.__name__,
                "description": "Short description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "f": {
                            "type": "number",
                            "description": "Float parameter.",
                        }
                    },
                    "required": ["f"],
                },
            }
            function_calling_schema = get_function_calling_schema(func)
            self.assertEqual(
                function_calling_schema,
                expected_function_calling_schema,
            )

    def test_function_with_str_parameter(self):
        def func_with_rest_style_docstring(s):
            """
            Short description.

            :param s: String parameter.
            :type s: str
            """
            pass

        def func_with_google_style_docstring(s):
            """
            Short description.

            Args:
                s (str): String parameter.
            """
            pass

        def func_with_numpy_style_docstring(s):
            """
            Short description.

            Parameters
            ----------
            s : str
                String parameter.
            """
            pass

        def func_with_rest_style_docstring_type_hinted(s: str):
            """
            Short description.

            :param s: String parameter.
            """
            pass

        def func_with_google_style_docstring_type_hinted(s: str):
            """
            Short description.

            Args:
                s: String parameter.
            """

        def func_with_numpy_style_docstring_type_hinted(s: str):
            """
            Short description.

            Parameters
            ----------
            s :
                String parameter.
            """
            pass

        for func in [
            func_with_rest_style_docstring,
            func_with_google_style_docstring,
            func_with_numpy_style_docstring,
            func_with_rest_style_docstring_type_hinted,
            func_with_google_style_docstring_type_hinted,
            func_with_numpy_style_docstring_type_hinted,
        ]:
            expected_function_calling_schema = {
                "name": func.__name__,
                "description": "Short description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "s": {
                            "type": "string",
                            "description": "String parameter.",
                        }
                    },
                    "required": ["s"],
                },
            }
            function_calling_schema = get_function_calling_schema(func)
            self.assertEqual(
                function_calling_schema,
                expected_function_calling_schema,
            )

    def test_function_with_bool_parameter(self):
        def func_with_rest_style_docstring(b):
            """
            Short description.

            :param b: Boolean parameter.
            :type b: bool
            """
            pass

        def func_with_google_style_docstring(b):
            """
            Short description.

            Args:
                b (bool): Boolean parameter.
            """
            pass

        def func_with_numpy_style_docstring(b):
            """
            Short description.

            Parameters
            ----------
            b : bool
                Boolean parameter.
            """
            pass

        def func_with_rest_style_docstring_type_hinted(b: bool):
            """
            Short description.

            :param b: Boolean parameter.
            """
            pass

        def func_with_google_style_docstring_type_hinted(b: bool):
            """
            Short description.

            Args:
                b: Boolean parameter.
            """
            pass

        def func_with_numpy_style_docstring_type_hinted(b: bool):
            """
            Short description.

            Parameters
            ----------
            b :
                Boolean parameter.
            """
            pass

        for func in [
            func_with_rest_style_docstring,
            func_with_google_style_docstring,
            func_with_numpy_style_docstring,
            func_with_rest_style_docstring_type_hinted,
            func_with_google_style_docstring_type_hinted,
            func_with_numpy_style_docstring_type_hinted,
        ]:
            expected_function_calling_schema = {
                "name": func.__name__,
                "description": "Short description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "b": {
                            "type": "boolean",
                            "description": "Boolean parameter.",
                        }
                    },
                    "required": ["b"],
                },
            }
            function_calling_schema = get_function_calling_schema(func)
            self.assertEqual(
                function_calling_schema,
                expected_function_calling_schema,
            )

    def test_function_with_list_parameter(self):
        def func_with_rest_style_docstring(l):
            """
            Short description.

            :param l: List parameter.
            :type l: list
            """
            pass

        def func_with_google_style_docstring(l):
            """
            Short description.

            Args:
                l (list): List parameter.
            """
            pass

        def func_with_numpy_style_docstring(l):
            """
            Short description.

            Parameters
            ----------
            l : list
                List parameter.
            """
            pass

        def func_with_rest_style_docstring_type_hinted(l: list):
            """
            Short description.

            :param l: List parameter.
            """
            pass

        def func_with_google_style_docstring_type_hinted(l: list):
            """
            Short description.

            Args:
                l: List parameter.
            """
            pass

        def func_with_numpy_style_docstring_type_hinted(l: list):
            """
            Short description.

            Parameters
            ----------
            l :
                List parameter.
            """
            pass

        for func in [
            func_with_rest_style_docstring,
            func_with_google_style_docstring,
            func_with_numpy_style_docstring,
            func_with_rest_style_docstring_type_hinted,
            func_with_google_style_docstring_type_hinted,
            func_with_numpy_style_docstring_type_hinted,
        ]:
            expected_function_calling_schema = {
                "name": func.__name__,
                "description": "Short description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "l": {
                            "type": "array",
                            "description": "List parameter.",
                        }
                    },
                    "required": ["l"],
                },
            }
            function_calling_schema = get_function_calling_schema(func)
            self.assertEqual(
                function_calling_schema,
                expected_function_calling_schema,
            )

    def test_function_with_dict_parameter(self):
        def func_with_rest_style_docstring(d):
            """
            Short description.

            :param d: Dictionary parameter.
            :type d: dict
            """
            pass

        def func_with_google_style_docstring(d):
            """
            Short description.

            Args:
                d (dict): Dictionary parameter.
            """
            pass

        def func_with_numpy_style_docstring(d):
            """
            Short description.

            Parameters
            ----------
            d : dict
                Dictionary parameter.
            """
            pass

        def func_with_rest_style_docstring_type_hinted(d: dict):
            """
            Short description.

            :param d: Dictionary parameter.
            """
            pass

        def func_with_google_style_docstring_type_hinted(d: dict):
            """
            Short description.

            Args:
                d: Dictionary parameter.
            """
            pass

        def func_with_numpy_style_docstring_type_hinted(d: dict):
            """
            Short description.

            Parameters
            ----------
            d :
                Dictionary parameter.
            """
            pass

        for func in [
            func_with_rest_style_docstring,
            func_with_google_style_docstring,
            func_with_numpy_style_docstring,
            func_with_rest_style_docstring_type_hinted,
            func_with_google_style_docstring_type_hinted,
            func_with_numpy_style_docstring_type_hinted,
        ]:
            expected_function_calling_schema = {
                "name": func.__name__,
                "description": "Short description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "d": {
                            "type": "object",
                            "description": "Dictionary parameter.",
                        }
                    },
                    "required": ["d"],
                },
            }
            function_calling_schema = get_function_calling_schema(func)
            self.assertEqual(
                function_calling_schema,
                expected_function_calling_schema,
            )

    def test_function_with_enum_str_parameter(self):
        def func_with_rest_style_docstring(s: Literal["a", "b"]):
            """
            Short description.

            :param s: String parameter.
            :type s: str
            """
            pass

        def func_with_google_style_docstring(s: Literal["a", "b"]):
            """
            Short description.

            Args:
                s (str): String parameter.
            """
            pass

        def func_with_numpy_style_docstring(s: Literal["a", "b"]):
            """
            Short description.

            Parameters
            ----------
            s : str
                String parameter.
            """
            pass

        def func_with_rest_style_docstring_type_hinted(s: Literal["a", "b"]):
            """
            Short description.

            :param s: String parameter.
            """
            pass

        def func_with_google_style_docstring_type_hinted(s: Literal["a", "b"]):
            """
            Short description.

            Args:
                s: String parameter.
            """
            pass

        def func_with_numpy_style_docstring_type_hinted(s: Literal["a", "b"]):
            """
            Short description.

            Parameters
            ----------
            s :
                String parameter.
            """
            pass

        for func in [
            func_with_rest_style_docstring,
            func_with_google_style_docstring,
            func_with_numpy_style_docstring,
            func_with_rest_style_docstring_type_hinted,
            func_with_google_style_docstring_type_hinted,
            func_with_numpy_style_docstring_type_hinted,
        ]:
            expected_function_calling_schema = {
                "name": func.__name__,
                "description": "Short description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "s": {
                            "type": "string",
                            "description": "String parameter.",
                            "enum": ["a", "b"],
                        }
                    },
                    "required": ["s"],
                },
            }
            function_calling_schema = get_function_calling_schema(func)
            self.assertEqual(
                function_calling_schema,
                expected_function_calling_schema,
            )

    def test_function_with_return(self):
        def func_with_rest_style_docstring():
            """
            Short description.

            :return: Return value.
            :rtype: int
            """
            pass

        def func_with_google_style_docstring():
            """
            Short description.

            Returns:
                int: Return value.
            """
            pass

        def func_with_numpy_style_docstring():
            """
            Short description.

            Returns
            -------
            int
                Return value.
            """
            pass

        for func in [
            func_with_rest_style_docstring,
            # func_with_google_style_docstring,
            # func_with_numpy_style_docstring,
        ]:
            expected_function_calling_schema = {
                "name": func.__name__,
                "description": "Short description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "return": {
                            "type": "number",
                            "description": "Return value.",
                        },
                    },
                    "required": ["return"],
                },

            }
            function_calling_schema = get_function_calling_schema(
                func,
                include_return_in_parameters=True,
            )
            self.assertEqual(
                function_calling_schema,
                expected_function_calling_schema,
            )

            expected_function_calling_schema = {
                "name": func.__name__,
                "description": "Short description.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            }
            function_calling_schema = get_function_calling_schema(
                func,
                include_return_in_parameters=False,
            )
            self.assertEqual(
                function_calling_schema,
                expected_function_calling_schema,
            )

    def test_function_with_multi_parameter(self):
        def func_with_rest_style_docstring(
            i: int,
            f: float,
            s: str,
            b: bool,
            l: list,
            d: dict,
            e: Literal["a", "b"],
            i_optional: int = 0,
            f_optional: float = 0.0,
            s_optional: str = "",
            b_optional: bool = False,
            l_optional: list = None,
            d_optional: dict = None,
            e_optional: Literal["a", "b"] = "a",
        ):
            """
            Short description.

            :param i: Integer parameter.
            :type i: int
            :param f: Float parameter.
            :type f: float
            :param s: String parameter.
            :type s: str
            :param b: Boolean parameter.
            :type b: bool
            :param l: List parameter.
            :type l: list
            :param d: Dictionary parameter.
            :type d: dict
            :param e: Enum parameter.
            :type e: Literal["a", "b"]
            :param i_optional: Optional integer parameter.
            :type i_optional: int
            :param f_optional: Optional float parameter.
            :type f_optional: float
            :param s_optional: Optional string parameter.
            :type s_optional: str
            :param b_optional: Optional boolean parameter.
            :type b_optional: bool
            :param l_optional: Optional list parameter.
            :type l_optional: list
            :param d_optional: Optional dictionary parameter.
            :type d_optional: dict
            :param e_optional: Optional enum parameter.
            :type e_optional: Literal["a", "b"]
            """
            pass

        def func_with_google_style_docstring(
            i: int,
            f: float,
            s: str,
            b: bool,
            l: list,
            d: dict,
            e: Literal["a", "b"],
            i_optional: int = 0,
            f_optional: float = 0.0,
            s_optional: str = "",
            b_optional: bool = False,
            l_optional: list = None,
            d_optional: dict = None,
            e_optional: Literal["a", "b"] = "a",
        ):
            """
            Short description.

            Args:
                i (int): Integer parameter.
                f (float): Float parameter.
                s (str): String parameter.
                b (bool): Boolean parameter.
                l (list): List parameter.
                d (dict): Dictionary parameter.
                e (Literal["a", "b"]): Enum parameter.
                i_optional (int, optional): Optional integer parameter.
                f_optional (float, optional): Optional float parameter.
                s_optional (str, optional): Optional string parameter.
                b_optional (bool, optional): Optional boolean parameter.
                l_optional (list, optional): Optional list parameter.
                d_optional (dict, optional): Optional dictionary parameter.
                e_optional (Literal["a", "b"], optional): Optional enum parameter.
            """
            pass

        def func_with_numpy_style_docstring(
            i: int,
            f: float,
            s: str,
            b: bool,
            l: list,
            d: dict,
            e: Literal["a", "b"],
            i_optional: int = 0,
            f_optional: float = 0.0,
            s_optional: str = "",
            b_optional: bool = False,
            l_optional: list = None,
            d_optional: dict = None,
            e_optional: Literal["a", "b"] = "a",
        ):
            """
            Short description.

            Parameters
            ----------
            i : int
                Integer parameter.
            f : float
                Float parameter.
            s : str
                String parameter.
            b : bool
                Boolean parameter.
            l : list
                List parameter.
            d : dict
                Dictionary parameter.
            e : Literal["a", "b"]
                Enum parameter.
            i_optional : int, optional
                Optional integer parameter.
            f_optional : float, optional
                Optional float parameter.
            s_optional : str, optional
                Optional string parameter.
            b_optional : bool, optional
                Optional boolean parameter.
            l_optional : list, optional
                Optional list parameter.
            d_optional : dict, optional
                Optional dictionary parameter.
            e_optional : Literal["a", "b"], optional
                Optional enum parameter.
            """
            pass

        for func in [
            func_with_rest_style_docstring,
            func_with_google_style_docstring,
            func_with_numpy_style_docstring,
        ]:
            expected_function_calling_schema = {
                "name": func.__name__,
                "description": "Short description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "i": {
                            "type": "number",
                            "description": "Integer parameter.",
                        },
                        "f": {
                            "type": "number",
                            "description": "Float parameter.",
                        },
                        "s": {
                            "type": "string",
                            "description": "String parameter.",
                        },
                        "b": {
                            "type": "boolean",
                            "description": "Boolean parameter.",
                        },
                        "l": {
                            "type": "array",
                            "description": "List parameter.",
                        },
                        "d": {
                            "type": "object",
                            "description": "Dictionary parameter.",
                        },
                        "e": {
                            "type": "string",
                            "description": "Enum parameter.",
                            "enum": ["a", "b"],
                        },
                        "i_optional": {
                            "type": "number",
                            "description": "Optional integer parameter.",
                        },
                        "f_optional": {
                            "type": "number",
                            "description": "Optional float parameter.",
                        },
                        "s_optional": {
                            "type": "string",
                            "description": "Optional string parameter.",
                        },
                        "b_optional": {
                            "type": "boolean",
                            "description": "Optional boolean parameter.",
                        },
                        "l_optional": {
                            "type": "array",
                            "description": "Optional list parameter.",
                        },
                        "d_optional": {
                            "type": "object",
                            "description": "Optional dictionary parameter.",
                        },
                        "e_optional": {
                            "type": "string",
                            "description": "Optional enum parameter.",
                            "enum": ["a", "b"],
                        },
                    },
                    "required": ["i", "f", "s", "b", "l", "d", "e"],
                },
            }
            function_calling_schema = get_function_calling_schema(func)
            self.assertEqual(
                function_calling_schema,
                expected_function_calling_schema,
            )
