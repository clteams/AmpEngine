#!/usr/bin/python3


class HandlerStart:
    def __init__(self):
        self.funcs = {}
        self.params_affected = {}

    def get_func(self, func_name):
        if func_name in self.funcs:
            return self.funcs[func_name]
        else:
            raise FunctionNotFound(func_name)

    def add_func(self, func_name, params_affected, value):
        self.funcs[func_name] = value
        self.params_affected[func_name] = params_affected

    def get_funcs_declaring(self, param):
        returned = []
        for pa_el in self.params_affected:
            if param in self.params_affected[pa_el]:
                returned.append(pa_el)
        return returned

    def get_all_funcs(self):
        return self.funcs.values()

    def get_func_params(self, func_name):
        return self.params_affected[func_name]


Handler = HandlerStart()


def new_func(func_name, params_affected):

    def segm_decorator(func):
        Handler.add_func(func_name, params_affected, func)

        def wrapped(function_arg1):
            return func(function_arg1)

        return wrapped

    return segm_decorator


@new_func('gram:case:set_loc', params_affected=['gram:case'])
def gram_case_set_loc(element, arguments=[], branching=[]):
    element.set_parameter('gram:case', 'loc')
    return element


class FunctionNotFound(Exception):
    pass
