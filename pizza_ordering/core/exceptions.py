class InvalidPizzaId(Exception):
    pass


class InvalidPizzaType(Exception):
    pass


class CannotCancelPizza(Exception):
    pass


class PizzaNotFound(Exception):
    pass

class PizzaRepoError(Exception):
    pass

class CoreError(Exception):
    pass

class ValidationError(Exception):
    pass

class UseCaseError(Exception):
    pass