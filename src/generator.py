"""
Math Problem Generator - Core functionality
Generates calculus problems with step-by-step solutions
"""

import random
from typing import Dict, List
import sympy as sp
from sympy import symbols, diff, integrate, limit, sin, cos, exp, log, oo


class ProblemGenerator:
    """Generates mathematical problems with solutions"""

    def __init__(self, seed: int = None):
        """
        Initialize generator with optional seed for reproducibility

        Args:
            seed: Random seed for reproducible problem generation
        """
        if seed is not None:
            random.seed(seed)
        self.x = symbols("x")

    def generate_derivative_problem(self, difficulty: str = "medium") -> Dict:
        """
        Generate a derivative problem with solution

        Args:
            difficulty: 'easy', 'medium', or 'hard'

        Returns:
            Dictionary with problem statement, solution, and steps
        """
        if difficulty == "easy":
            function = self._generate_polynomial(max_degree=2)
        elif difficulty == "medium":
            function = self._generate_polynomial(max_degree=3) + random.choice(
                [sin(self.x), cos(self.x)]
            )
        else:  # hard
            function = self._generate_complex_function()

        derivative = diff(function, self.x)

        return {
            "type": "derivative",
            "difficulty": difficulty,
            "function": str(function),
            "function_latex": sp.latex(function),
            "solution": str(derivative),
            "solution_latex": sp.latex(derivative),
            "steps": self._generate_derivative_steps(function),
        }

    def generate_integral_problem(self, difficulty: str = "medium") -> Dict:
        """
        Generate an integral problem with solution

        Args:
            difficulty: 'easy', 'medium', or 'hard'

        Returns:
            Dictionary with problem statement, solution, and steps
        """
        if difficulty == "easy":
            function = self._generate_polynomial(max_degree=2)
        elif difficulty == "medium":
            function = self._generate_polynomial(max_degree=2) * random.choice(
                [sin(self.x), cos(self.x)]
            )
        else:  # hard
            function = self._generate_rational_function()

        integral = integrate(function, self.x)

        return {
            "type": "integral",
            "difficulty": difficulty,
            "function": str(function),
            "function_latex": sp.latex(function),
            "solution": str(integral),
            "solution_latex": sp.latex(integral),
            "steps": self._generate_integral_steps(function),
        }

    def generate_limit_problem(self, difficulty: str = "medium") -> Dict:
        """
        Generate a limit problem with solution

        Args:
            difficulty: 'easy', 'medium', or 'hard'

        Returns:
            Dictionary with problem statement, solution, and steps
        """
        point = random.choice([0, 1, oo])

        if difficulty == "easy":
            function = self._generate_polynomial(max_degree=2)
        elif difficulty == "medium":
            # Create indeterminate form
            numerator = self.x**2 - 1
            denominator = self.x - 1
            function = numerator / denominator
            point = 1
        else:  # hard
            function = sin(self.x) / self.x
            point = 0

        try:
            limit_result = limit(function, self.x, point)
        except Exception:
            limit_result = "undefined"

        return {
            "type": "limit",
            "difficulty": difficulty,
            "function": str(function),
            "function_latex": sp.latex(function),
            "point": str(point),
            "solution": str(limit_result),
            "solution_latex": (
                sp.latex(limit_result) if limit_result != "undefined" else "undefined"
            ),
            "steps": self._generate_limit_steps(function, point),
        }

    def generate_problem_set(
        self,
        count: int = 5,
        problem_types: List[str] = None,
        difficulty: str = "medium",
    ) -> List[Dict]:
        """
        Generate a set of problems

        Args:
            count: Number of problems to generate
            problem_types: List of problem types ('derivative', 'integral', 'limit')
            difficulty: Difficulty level

        Returns:
            List of problem dictionaries
        """
        if problem_types is None:
            problem_types = ["derivative", "integral", "limit"]

        problems = []
        for i in range(count):
            problem_type = random.choice(problem_types)

            if problem_type == "derivative":
                problem = self.generate_derivative_problem(difficulty)
            elif problem_type == "integral":
                problem = self.generate_integral_problem(difficulty)
            else:
                problem = self.generate_limit_problem(difficulty)

            problem["number"] = i + 1
            problems.append(problem)

        return problems

    def _generate_polynomial(self, max_degree: int = 3) -> sp.Expr:
        """Generate a random polynomial"""
        degree = random.randint(1, max_degree)
        coeffs = [random.randint(-5, 5) for _ in range(degree + 1)]
        # Ensure leading coefficient is not zero
        if coeffs[-1] == 0:
            coeffs[-1] = random.choice([1, 2, -1, -2])

        poly = sum(c * self.x**i for i, c in enumerate(coeffs))
        return poly

    def _generate_complex_function(self) -> sp.Expr:
        """Generate a more complex function"""
        choices = [
            exp(self.x) * sin(self.x),
            self.x * log(self.x),
            sin(self.x) * cos(self.x),
            exp(self.x**2),
        ]
        return random.choice(choices)

    def _generate_rational_function(self) -> sp.Expr:
        """Generate a rational function"""
        numerator = self._generate_polynomial(max_degree=2)
        denominator = self._generate_polynomial(max_degree=2)
        return numerator / denominator

    def _generate_derivative_steps(self, function: sp.Expr) -> List[str]:
        """Generate step-by-step solution for derivative"""
        steps = [
            f"Given function: f(x) = {function}",
            "Apply derivative rules:",
        ]

        # Add specific rules based on function structure
        if function.has(sin):
            steps.append("- Derivative of sin(x) is cos(x)")
        if function.has(cos):
            steps.append("- Derivative of cos(x) is -sin(x)")
        if function.has(exp):
            steps.append("- Derivative of e^x is e^x")

        derivative = diff(function, self.x)
        steps.append(f"Result: f'(x) = {derivative}")

        return steps

    def _generate_integral_steps(self, function: sp.Expr) -> List[str]:
        """Generate step-by-step solution for integral"""
        steps = [
            f"Given function: f(x) = {function}",
            "Apply integration rules:",
        ]

        integral = integrate(function, self.x)
        steps.append(f"Result: ∫f(x)dx = {integral} + C")

        return steps

    def _generate_limit_steps(self, function: sp.Expr, point) -> List[str]:
        """Generate step-by-step solution for limit"""
        steps = [
            f"Given function: f(x) = {function}",
            f"Find limit as x → {point}",
        ]

        # Check for indeterminate form
        try:
            direct_sub = function.subs(self.x, point)
            steps.append(f"Direct substitution: {direct_sub}")
        except Exception:
            steps.append("Direct substitution leads to indeterminate form")
            steps.append("Apply L'Hôpital's rule or algebraic manipulation")

        try:
            result = limit(function, self.x, point)
            steps.append(f"Result: lim(x→{point}) f(x) = {result}")
        except Exception:
            steps.append("Limit is undefined or does not exist")

        return steps
