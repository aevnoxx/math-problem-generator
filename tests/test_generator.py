"""
Unit tests for ProblemGenerator
"""

import pytest
from src.generator import ProblemGenerator


class TestProblemGenerator:
    """Test cases for ProblemGenerator class"""

    def setup_method(self):
        """Setup test fixtures"""
        self.generator = ProblemGenerator(seed=42)

    def test_initialization(self):
        """Test generator initialization"""
        generator = ProblemGenerator()
        assert generator is not None
        assert generator.x is not None

    def test_initialization_with_seed(self):
        """Test generator with seed initialization"""
        gen1 = ProblemGenerator(seed=123)
        gen2 = ProblemGenerator(seed=123)

        # Generators should be initialized successfully
        assert gen1 is not None
        assert gen2 is not None

        # Both should produce valid problems
        prob1 = gen1.generate_derivative_problem()
        prob2 = gen2.generate_derivative_problem()

        assert "function" in prob1
        assert "function" in prob2

    def test_generate_derivative_problem_structure(self):
        """Test derivative problem has correct structure"""
        problem = self.generator.generate_derivative_problem()

        assert "type" in problem
        assert "difficulty" in problem
        assert "function" in problem
        assert "function_latex" in problem
        assert "solution" in problem
        assert "solution_latex" in problem
        assert "steps" in problem

        assert problem["type"] == "derivative"

    def test_generate_derivative_easy(self):
        """Test easy derivative problem generation"""
        problem = self.generator.generate_derivative_problem(difficulty="easy")

        assert problem["difficulty"] == "easy"
        assert problem["function"] is not None
        assert problem["solution"] is not None

    def test_generate_derivative_medium(self):
        """Test medium derivative problem generation"""
        problem = self.generator.generate_derivative_problem(difficulty="medium")

        assert problem["difficulty"] == "medium"
        assert problem["function"] is not None

    def test_generate_derivative_hard(self):
        """Test hard derivative problem generation"""
        problem = self.generator.generate_derivative_problem(difficulty="hard")

        assert problem["difficulty"] == "hard"
        assert problem["function"] is not None

    def test_generate_integral_problem_structure(self):
        """Test integral problem has correct structure"""
        problem = self.generator.generate_integral_problem()

        assert "type" in problem
        assert problem["type"] == "integral"
        assert "function" in problem
        assert "solution" in problem

    def test_generate_integral_difficulty_levels(self):
        """Test integral generation for all difficulty levels"""
        for difficulty in ["easy", "medium", "hard"]:
            problem = self.generator.generate_integral_problem(difficulty=difficulty)
            assert problem["difficulty"] == difficulty
            assert problem["function"] is not None

    def test_generate_limit_problem_structure(self):
        """Test limit problem has correct structure"""
        problem = self.generator.generate_limit_problem()

        assert "type" in problem
        assert problem["type"] == "limit"
        assert "function" in problem
        assert "point" in problem
        assert "solution" in problem

    def test_generate_limit_difficulty_levels(self):
        """Test limit generation for all difficulty levels"""
        for difficulty in ["easy", "medium", "hard"]:
            problem = self.generator.generate_limit_problem(difficulty=difficulty)
            assert problem["difficulty"] == difficulty

    def test_generate_problem_set_default(self):
        """Test generating default problem set"""
        problems = self.generator.generate_problem_set()

        assert len(problems) == 5
        assert all("number" in p for p in problems)
        assert all("type" in p for p in problems)

    def test_generate_problem_set_custom_count(self):
        """Test generating custom number of problems"""
        count = 10
        problems = self.generator.generate_problem_set(count=count)

        assert len(problems) == count

    def test_generate_problem_set_specific_types(self):
        """Test generating only specific problem types"""
        problems = self.generator.generate_problem_set(
            count=6, problem_types=["derivative"]
        )

        assert len(problems) == 6
        assert all(p["type"] == "derivative" for p in problems)

    def test_generate_problem_set_mixed_types(self):
        """Test generating mixed problem types"""
        problems = self.generator.generate_problem_set(
            count=9, problem_types=["derivative", "integral", "limit"]
        )

        types = set(p["type"] for p in problems)
        assert len(types) >= 1  # At least one type should be present

    def test_generate_problem_set_custom_difficulty(self):
        """Test generating problems with custom difficulty"""
        problems = self.generator.generate_problem_set(count=5, difficulty="hard")

        assert all(p["difficulty"] == "hard" for p in problems)

    def test_problem_numbering(self):
        """Test that problems are numbered correctly"""
        problems = self.generator.generate_problem_set(count=5)

        numbers = [p["number"] for p in problems]
        assert numbers == list(range(1, 6))

    def test_steps_are_lists(self):
        """Test that steps are returned as lists"""
        problem = self.generator.generate_derivative_problem()

        assert isinstance(problem["steps"], list)
        assert len(problem["steps"]) > 0
        assert all(isinstance(step, str) for step in problem["steps"])

    def test_latex_output_not_empty(self):
        """Test that LaTeX output is generated"""
        problem = self.generator.generate_derivative_problem()

        assert problem["function_latex"] != ""
        assert problem["solution_latex"] != ""

    def test_different_seeds_produce_different_problems(self):
        """Test that different seeds produce different problems"""
        gen1 = ProblemGenerator(seed=1)
        gen2 = ProblemGenerator(seed=2)

        prob1 = gen1.generate_derivative_problem()
        prob2 = gen2.generate_derivative_problem()

        # Should be different with high probability
        assert prob1["function"] != prob2["function"]
