import json
import re
import os

def create_ch1_questions():
    # Chapter 1: Circular Functions and Trigonometry
    # Focus: Trig identities, degree/radian conversion, trigonometric equations, double angle formulas.
    easy = [
        {"q": "Convert 180 degrees to radians.", "opts": {"a": "π radians", "b": "π/2 radians", "c": "2π radians", "d": "3π/2 radians"}, "ans": "a"},
        {"q": "What is the value of sin(π/6)?", "opts": {"a": "1/2", "b": "√3/2", "c": "√2/2", "d": "1"}, "ans": "a"},
        {"q": "What is the value of cos(π/3)?", "opts": {"a": "1/2", "b": "√3/2", "c": "√2/2", "d": "0"}, "ans": "a"},
        {"q": "Which of the following is the fundamental trigonometric identity?", "opts": {"a": "sin²(θ) + cos²(θ) = 1", "b": "sin(θ) + cos(θ) = 1", "c": "tan²(θ) + 1 = sin²(θ)", "d": "cos²(θ) - sin²(θ) = 1"}, "ans": "a"},
        {"q": "What is the value of tan(π/4)?", "opts": {"a": "1", "b": "0", "c": "√3", "d": "1/√3"}, "ans": "a"},
        {"q": "Convert 90 degrees to radians.", "opts": {"a": "π/2 radians", "b": "π radians", "c": "π/4 radians", "d": "3π/2 radians"}, "ans": "a"},
        {"q": "What is the value of sin(0)?", "opts": {"a": "0", "b": "1", "c": "-1", "d": "1/2"}, "ans": "a"},
        {"q": "What is the value of cos(0)?", "opts": {"a": "1", "b": "0", "c": "-1", "d": "1/2"}, "ans": "a"},
        {"q": "Which quadrant is the angle 150 degrees located in?", "opts": {"a": "Quadrant II", "b": "Quadrant I", "c": "Quadrant III", "d": "Quadrant IV"}, "ans": "a"},
        {"q": "In a right-angled triangle, what is the sine of an angle defined as?", "opts": {"a": "Opposite / Hypotenuse", "b": "Adjacent / Hypotenuse", "c": "Opposite / Adjacent", "d": "Adjacent / Opposite"}, "ans": "a"},
        {"q": "In a right-angled triangle, what is the cosine of an angle defined as?", "opts": {"a": "Adjacent / Hypotenuse", "b": "Opposite / Hypotenuse", "c": "Opposite / Adjacent", "d": "Adjacent / Opposite"}, "ans": "a"},
        {"q": "In a right-angled triangle, what is the tangent of an angle defined as?", "opts": {"a": "Opposite / Adjacent", "b": "Opposite / Hypotenuse", "c": "Adjacent / Hypotenuse", "d": "Adjacent / Opposite"}, "ans": "a"},
        {"q": "What is the value of sin(π)?", "opts": {"a": "0", "b": "1", "c": "-1", "d": "1/2"}, "ans": "a"},
        {"q": "What is the value of cos(π)?", "opts": {"a": "-1", "b": "0", "c": "1", "d": "-1/2"}, "ans": "a"},
        {"q": "What is the period of the function f(x) = sin(x)?", "opts": {"a": "2π", "b": "π", "c": "π/2", "d": "4π"}, "ans": "a"},
        {"q": "What is the period of the function f(x) = tan(x)?", "opts": {"a": "π", "b": "2π", "c": "π/2", "d": "3π"}, "ans": "a"},
        {"q": "Convert 30 degrees to radians.", "opts": {"a": "π/6 radians", "b": "π/3 radians", "c": "π/4 radians", "d": "π/2 radians"}, "ans": "a"},
        {"q": "Convert 60 degrees to radians.", "opts": {"a": "π/3 radians", "b": "π/6 radians", "c": "π/4 radians", "d": "π/2 radians"}, "ans": "a"},
        {"q": "What is the reciprocal of the sine function?", "opts": {"a": "Cosecant (csc)", "b": "Secant (sec)", "c": "Cotangent (cot)", "d": "Cosine (cos)"}, "ans": "a"},
        {"q": "What is the reciprocal of the cosine function?", "opts": {"a": "Secant (sec)", "b": "Cosecant (csc)", "c": "Cotangent (cot)", "d": "Sine (sin)"}, "ans": "a"},
        {"q": "What is the reciprocal of the tangent function?", "opts": {"a": "Cotangent (cot)", "b": "Secant (sec)", "c": "Cosecant (csc)", "d": "Sine (sin)"}, "ans": "a"},
        {"q": "What is the value of sin(3π/2)?", "opts": {"a": "-1", "b": "0", "c": "1", "d": "√3/2"}, "ans": "a"},
        {"q": "What is the value of cos(3π/2)?", "opts": {"a": "0", "b": "1", "c": "-1", "d": "-1/2"}, "ans": "a"},
        {"q": "Convert 45 degrees to radians.", "opts": {"a": "π/4 radians", "b": "π/2 radians", "c": "π/3 radians", "d": "π/6 radians"}, "ans": "a"},
        {"q": "What is the value of tan(0)?", "opts": {"a": "0", "b": "1", "c": "undefined", "d": "-1"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "Solve for x in the interval [0, 2π]: 2 sin(x) - 1 = 0.", "opts": {"a": "π/6 and 5π/6", "b": "π/3 and 2π/3", "c": "π/4 and 3π/4", "d": "π/6 and 7π/6"}, "ans": "a"},
        {"q": "What is the double-angle formula for sin(2θ)?", "opts": {"a": "2 sin(θ) cos(θ)", "b": "cos²(θ) - sin²(θ)", "c": "2 sin(θ)", "d": "sin²(θ) - cos²(θ)"}, "ans": "a"},
        {"q": "What is the double-angle formula for cos(2θ)?", "opts": {"a": "cos²(θ) - sin²(θ)", "b": "2 sin(θ) cos(θ)", "c": "2 cos(θ)", "d": "1 + sin²(θ)"}, "ans": "a"},
        {"q": "Simplify the expression: sec(x) * cos(x).", "opts": {"a": "1", "b": "sin(x)", "c": "tan(x)", "d": "csc(x)"}, "ans": "a"},
        {"q": "Simplify the expression: csc(x) * sin(x).", "opts": {"a": "1", "b": "cos(x)", "c": "cot(x)", "d": "sec(x)"}, "ans": "a"},
        {"q": "Simplify the expression: tan(x) * cos(x).", "opts": {"a": "sin(x)", "b": "1", "c": "cos(x)", "d": "sec(x)"}, "ans": "a"},
        {"q": "Simplify the expression: cot(x) * sin(x).", "opts": {"a": "cos(x)", "b": "sin(x)", "c": "1", "d": "csc(x)"}, "ans": "a"},
        {"q": "If sin(θ) = 3/5 and θ is in Quadrant I, what is the value of cos(θ)?", "opts": {"a": "4/5", "b": "3/4", "c": "5/4", "d": "2/5"}, "ans": "a"},
        {"q": "If cos(θ) = 5/13 and θ is in Quadrant I, what is the value of sin(θ)?", "opts": {"a": "12/13", "b": "12/5", "c": "13/12", "d": "5/12"}, "ans": "a"},
        {"q": "What is the value of sin(-x) according to negative angle identities?", "opts": {"a": "-sin(x)", "b": "sin(x)", "c": "cos(x)", "d": "-cos(x)"}, "ans": "a"},
        {"q": "What is the value of cos(-x) according to negative angle identities?", "opts": {"a": "cos(x)", "b": "-cos(x)", "c": "sin(x)", "d": "-sin(x)"}, "ans": "a"},
        {"q": "Solve for x in [0, 2π]: cos(x) = 1/2.", "opts": {"a": "π/3 and 5π/3", "b": "π/6 and 11π/6", "c": "π/3 and 2π/3", "d": "π/4 and 7π/4"}, "ans": "a"},
        {"q": "Evaluate sin(5π/6).", "opts": {"a": "1/2", "b": "-1/2", "c": "√3/2", "d": "-√3/2"}, "ans": "a"},
        {"q": "Evaluate cos(5π/6).", "opts": {"a": "-√3/2", "b": "√3/2", "c": "-1/2", "d": "1/2"}, "ans": "a"},
        {"q": "Evaluate sin(4π/3).", "opts": {"a": "-√3/2", "b": "-1/2", "c": "√3/2", "d": "1/2"}, "ans": "a"},
        {"q": "Evaluate cos(4π/3).", "opts": {"a": "-1/2", "b": "-√3/2", "c": "1/2", "d": "√3/2"}, "ans": "a"},
        {"q": "What is the value of 1 + tan²(θ) according to Pythagorean identities?", "opts": {"a": "sec²(θ)", "b": "csc²(θ)", "c": "cot²(θ)", "d": "cos²(θ)"}, "ans": "a"},
        {"q": "What is the value of 1 + cot²(θ) according to Pythagorean identities?", "opts": {"a": "csc²(θ)", "b": "sec²(θ)", "c": "tan²(θ)", "d": "sin²(θ)"}, "ans": "a"},
        {"q": "Convert 3π/4 radians to degrees.", "opts": {"a": "135 degrees", "b": "120 degrees", "c": "150 degrees", "d": "145 degrees"}, "ans": "a"},
        {"q": "Convert 2π/3 radians to degrees.", "opts": {"a": "120 degrees", "b": "135 degrees", "c": "150 degrees", "d": "115 degrees"}, "ans": "a"},
        {"q": "Convert 7π/6 radians to degrees.", "opts": {"a": "210 degrees", "b": "225 degrees", "c": "240 degrees", "d": "190 degrees"}, "ans": "a"},
        {"q": "If tan(θ) = 3/4 and θ is in Quadrant I, what is csc(θ)?", "opts": {"a": "5/3", "b": "5/4", "c": "4/3", "d": "3/5"}, "ans": "a"},
        {"q": "Solve for x in [0, π]: sin(2x) = 1.", "opts": {"a": "π/4", "b": "π/2", "c": "π/8", "d": "3π/4"}, "ans": "a"},
        {"q": "Simplify: (1 - sin²(x)) / cos²(x).", "opts": {"a": "1", "b": "tan²(x)", "c": "sec²(x)", "d": "0"}, "ans": "a"},
        {"q": "Evaluate tan(3π/4).", "opts": {"a": "-1", "b": "1", "c": "√3", "d": "-√3"}, "ans": "a"},
        {"q": "If sin(x) = cos(x) in the interval [0, π], what is x?", "opts": {"a": "π/4", "b": "3π/4", "c": "π/2", "d": "π/6"}, "ans": "a"},
        {"q": "Express sin(A + B) using sum identity.", "opts": {"a": "sin(A)cos(B) + cos(A)sin(B)", "b": "sin(A)sin(B) + cos(A)cos(B)", "c": "sin(A)cos(B) - cos(A)sin(B)", "d": "cos(A)cos(B) - sin(A)sin(B)"}, "ans": "a"},
        {"q": "Express cos(A + B) using sum identity.", "opts": {"a": "cos(A)cos(B) - sin(A)sin(B)", "b": "cos(A)cos(B) + sin(A)sin(B)", "c": "sin(A)cos(B) + cos(A)sin(B)", "d": "sin(A)sin(B) - cos(A)cos(B)"}, "ans": "a"},
        {"q": "Find the amplitude of the function f(x) = -3 sin(2x + 1).", "opts": {"a": "3", "b": "-3", "c": "2", "d": "1"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Solve the equation for x in [0, 2π]: 2 cos²(x) + cos(x) - 1 = 0.", "opts": {"a": "π/3, π, and 5π/3", "b": "π/6, π, and 11π/6", "c": "π/3, 2π/3, and π", "d": "π/4, π, and 7π/4"}, "ans": "a"},
        {"q": "If sin(A) = 3/5, cos(B) = 12/13, and both angles are in Quadrant I, find the value of sin(A + B).", "opts": {"a": "56/65", "b": "33/65", "c": "16/65", "d": "63/65"}, "ans": "a"},
        {"q": "If sin(A) = 3/5, cos(B) = 12/13, and both angles are in Quadrant I, find the value of cos(A + B).", "opts": {"a": "33/65", "b": "56/65", "c": "16/65", "d": "25/65"}, "ans": "a"},
        {"q": "Solve for x in the interval [0, π]: sin(3x) = 0.", "opts": {"a": "0, π/3, 2π/3, and π", "b": "0, π/6, π/2, and 5π/6", "c": "π/6, π/2, and 5π/6", "d": "0, π/4, π/2, and 3π/4"}, "ans": "a"},
        {"q": "Evaluate: sin(π/12). Hint: Use half-angle or sum/difference formula.", "opts": {"a": "(√6 - √2)/4", "b": "(√6 + √2)/4", "c": "(√3 - 1)/2", "d": "(√2 - 1)/2"}, "ans": "a"},
        {"q": "Evaluate: cos(π/12). Hint: Use half-angle or sum/difference formula.", "opts": {"a": "(√6 + √2)/4", "b": "(√6 - √2)/4", "c": "(√3 + 1)/2", "d": "(√2 + 1)/2"}, "ans": "a"},
        {"q": "Simplify the expression: (sin(2x)) / (1 + cos(2x)).", "opts": {"a": "tan(x)", "b": "cot(x)", "c": "sin(x)", "d": "cos(x)"}, "ans": "a"},
        {"q": "Simplify the expression: (1 - cos(2x)) / (sin(2x)).", "opts": {"a": "tan(x)", "b": "cot(x)", "c": "cos(x)", "d": "1"}, "ans": "a"},
        {"q": "Solve for x in [0, 2π]: sin(x) + cos(x) = 1.", "opts": {"a": "0 and π/2", "b": "π/4 and 3π/4", "c": "0 and π", "d": "π/2 and π"}, "ans": "a"},
        {"q": "Solve for x in [0, 2π]: sin(x) - cos(x) = 1.", "opts": {"a": "π/2 and π", "b": "0 and π/2", "c": "3π/4 and 7π/4", "d": "π and 3π/2"}, "ans": "a"},
        {"q": "Evaluate: sin(7π/12).", "opts": {"a": "(√6 + √2)/4", "b": "(√6 - √2)/4", "c": "(√3 + 1)/2", "d": "(√2 + 1)/2"}, "ans": "a"},
        {"q": "Find all solutions to: tan²(x) - 3 = 0 in [0, 2π].", "opts": {"a": "π/3, 2π/3, 4π/3, and 5π/3", "b": "π/6, 5π/6, 7π/6, and 11π/6", "c": "π/4, 3π/4, 5π/4, and 7π/4", "d": "π/3 and 4π/3"}, "ans": "a"},
        {"q": "Simplify: sin(x + π/2).", "opts": {"a": "cos(x)", "b": "-cos(x)", "c": "sin(x)", "d": "-sin(x)"}, "ans": "a"},
        {"q": "Simplify: cos(x + π/2).", "opts": {"a": "-sin(x)", "b": "sin(x)", "c": "cos(x)", "d": "-cos(x)"}, "ans": "a"},
        {"q": "Express cos(3x) in terms of cos(x).", "opts": {"a": "4 cos³(x) - 3 cos(x)", "b": "3 cos(x) - 4 cos³(x)", "c": "cos³(x) - 3 cos(x)", "d": "4 cos³(x) + 3 cos(x)"}, "ans": "a"},
        {"q": "Express sin(3x) in terms of sin(x).", "opts": {"a": "3 sin(x) - 4 sin³(x)", "b": "4 sin³(x) - 3 sin(x)", "c": "3 sin³(x) - 4 sin(x)", "d": "4 sin³(x) + 3 sin(x)"}, "ans": "a"},
        {"q": "If sec²(θ) + tan²(θ) = 7, solve for θ in [0, π/2].", "opts": {"a": "π/3", "b": "π/6", "c": "π/4", "d": "π/12"}, "ans": "a"},
        {"q": "If csc²(θ) + cot²(θ) = 5, solve for θ in [0, π/2].", "opts": {"a": "π/6", "b": "π/3", "c": "π/4", "d": "π/8"}, "ans": "a"},
        {"q": "If sin(θ) = -1/3 and θ is in Quadrant III, find cos(θ/2).", "opts": {"a": "-√((3-2√2)/6)", "b": "-√((3+2√2)/6)", "c": "√((3-2√2)/6)", "d": "√((3+2√2)/6)"}, "ans": "a"},
        {"q": "Find the general solution to: 2 sin(3x) = √3.", "opts": {"a": "x = π/9 + 2nπ/3 or x = 2π/9 + 2nπ/3", "b": "x = π/6 + 2nπ/3 or x = 5π/6 + 2nπ/3", "c": "x = π/9 + nπ or x = 2π/9 + nπ", "d": "x = π/3 + 2nπ/3"}, "ans": "a"},
        {"q": "Evaluate: tan(π/12).", "opts": {"a": "2 - √3", "b": "2 + √3", "c": "√3 - 1", "d": "√3 - 2"}, "ans": "a"},
        {"q": "Simplify: (cos(x) - sin(x)) / (cos(x) + sin(x)).", "opts": {"a": "tan(π/4 - x)", "b": "tan(π/4 + x)", "c": "cot(π/4 - x)", "d": "cot(π/4 + x)"}, "ans": "a"},
        {"q": "If tan(A) = 1/2 and tan(B) = 1/3, find the value of A + B in [0, π/2].", "opts": {"a": "π/4", "b": "π/6", "c": "π/3", "d": "π/12"}, "ans": "a"},
        {"q": "In a triangle ABC, if a = 5, b = 7, and C = 60°, find the length of side c.", "opts": {"a": "√39", "b": "39", "c": "√74", "d": "√109"}, "ans": "a"},
        {"q": "In a triangle ABC, if a = 3, b = 5, and c = 7, find the angle C.", "opts": {"a": "120°", "b": "60°", "c": "150°", "d": "90°"}, "ans": "a"},
        {"q": "What is the range of the function f(x) = 2 cos(3x) - 1?", "opts": {"a": "[-3, 1]", "b": "[-1, 1]", "c": "[-2, 2]", "d": "[-3, 3]"}, "ans": "a"},
        {"q": "If sin(x) + cos(x) = √2, what is the value of sin(2x)?", "opts": {"a": "1", "b": "1/2", "c": "0", "d": "-1"}, "ans": "a"},
        {"q": "Find all solutions of: 2 sin²(x) - 3 sin(x) + 1 = 0 in [0, 2π].", "opts": {"a": "π/6, π/2, and 5π/6", "b": "π/6, π/3, and 5π/6", "c": "π/4, π/2, and 3π/4", "d": "π/6, 5π/6, and 7π/6"}, "ans": "a"},
        {"q": "Evaluate: cos(7π/6).", "opts": {"a": "-√3/2", "b": "√3/2", "c": "-1/2", "d": "1/2"}, "ans": "a"},
        {"q": "Simplify: sin²(x) * cot²(x) + cos²(x) * tan²(x).", "opts": {"a": "1", "b": "2", "c": "sin²(x)", "d": "cos²(x)"}, "ans": "a"},
        {"q": "Evaluate: sin(11π/6).", "opts": {"a": "-1/2", "b": "1/2", "c": "-√3/2", "d": "√3/2"}, "ans": "a"},
        {"q": "If sin(x)cos(x) = 1/4, find the value of sin(2x).", "opts": {"a": "1/2", "b": "1/4", "c": "1", "d": "√3/2"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch2_questions():
    # Chapter 2: Analytic Geometry
    # Focus: Slope, equations of lines, distance formula, midpoint formula, parallel/perpendicular lines.
    easy = [
        {"q": "What is the formula for the distance between two points (x1, y1) and (x2, y2)?", "opts": {"a": "√((x2 - x1)² + (y2 - y1)²)", "b": "(x2 - x1)² + (y2 - y1)²", "c": "√((x2 + x1)² + (y2 + y1)²)", "d": "((x2 - x1) + (y2 - y1))/2"}, "ans": "a"},
        {"q": "Find the slope of the line passing through (2, 3) and (5, 9).", "opts": {"a": "2", "b": "1/2", "c": "3", "d": "-2"}, "ans": "a"},
        {"q": "What is the midpoint of the line segment joining (4, 8) and (8, 2)?", "opts": {"a": "(6, 5)", "b": "(12, 10)", "c": "(2, 3)", "d": "(5, 6)"}, "ans": "a"},
        {"q": "What is the slope-intercept form of a linear equation?", "opts": {"a": "y = mx + c", "b": "ax + by + c = 0", "c": "y - y1 = m(x - x1)", "d": "x/a + y/b = 1"}, "ans": "a"},
        {"q": "What is the slope of the line y = -4x + 7?", "opts": {"a": "-4", "b": "4", "c": "7", "d": "-7"}, "ans": "a"},
        {"q": "What is the y-intercept of the line y = 3x - 5?", "opts": {"a": "-5", "b": "3", "c": "5", "d": "0"}, "ans": "a"},
        {"q": "Find the slope of a line parallel to the line y = 5x - 3.", "opts": {"a": "5", "b": "-5", "c": "-1/5", "d": "1/5"}, "ans": "a"},
        {"q": "Find the slope of a line perpendicular to the line y = 2x + 1.", "opts": {"a": "-1/2", "b": "1/2", "c": "-2", "d": "2"}, "ans": "a"},
        {"q": "What is the slope of a horizontal line?", "opts": {"a": "0", "b": "undefined", "c": "1", "d": "-1"}, "ans": "a"},
        {"q": "What is the slope of a vertical line?", "opts": {"a": "undefined", "b": "0", "c": "1", "d": "-1"}, "ans": "a"},
        {"q": "Find the distance between the origin (0, 0) and the point (3, 4).", "opts": {"a": "5", "b": "25", "c": "7", "d": "√7"}, "ans": "a"},
        {"q": "Find the slope of the line passing through (1, 1) and (4, 4).", "opts": {"a": "1", "b": "0", "c": "3", "d": "-1"}, "ans": "a"},
        {"q": "What is the equation of the line passing through (0, 0) with a slope of 3?", "opts": {"a": "y = 3x", "b": "y = x/3", "c": "y = 3", "d": "x = 3"}, "ans": "a"},
        {"q": "What is the equation of a vertical line passing through the point (5, -2)?", "opts": {"a": "x = 5", "b": "y = -2", "c": "x = -2", "d": "y = 5"}, "ans": "a"},
        {"q": "What is the equation of a horizontal line passing through the point (5, -2)?", "opts": {"a": "y = -2", "b": "x = 5", "c": "y = 5", "d": "x = -2"}, "ans": "a"},
        {"q": "Find the midpoint between (-2, 5) and (4, -1).", "opts": {"a": "(1, 2)", "b": "(2, 4)", "c": "(3, 3)", "d": "(-1, 2)"}, "ans": "a"},
        {"q": "Find the slope of the line passing through (-1, 2) and (3, -6).", "opts": {"a": "-2", "b": "2", "c": "-1/2", "d": "1/2"}, "ans": "a"},
        {"q": "What is the distance between points (1, 2) and (1, 10)?", "opts": {"a": "8", "b": "12", "c": "√8", "d": "6"}, "ans": "a"},
        {"q": "If the slope of a line is 0, the line is:", "opts": {"a": "horizontal", "b": "vertical", "c": "slanted upwards", "d": "slanted downwards"}, "ans": "a"},
        {"q": "If the slope of a line is undefined, the line is:", "opts": {"a": "vertical", "b": "horizontal", "c": "slanted upwards", "d": "slanted downwards"}, "ans": "a"},
        {"q": "Find the y-intercept of the line 2x - 3y = 6.", "opts": {"a": "-2", "b": "2", "c": "3", "d": "-3"}, "ans": "a"},
        {"q": "Find the x-intercept of the line 2x - 3y = 6.", "opts": {"a": "3", "b": "-3", "c": "2", "d": "-2"}, "ans": "a"},
        {"q": "Find the slope of the line 4x + 2y = 8.", "opts": {"a": "-2", "b": "2", "c": "-4", "d": "4"}, "ans": "a"},
        {"q": "What is the distance between points (-3, 0) and (3, 0)?", "opts": {"a": "6", "b": "0", "c": "3", "d": "√6"}, "ans": "a"},
        {"q": "Find the midpoint between (0, 0) and (6, 8).", "opts": {"a": "(3, 4)", "b": "(6, 4)", "c": "(3, 8)", "d": "(4, 3)"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "Find the equation of the line passing through (2, 5) with a slope of -3.", "opts": {"a": "y = -3x + 11", "b": "y = -3x - 1", "c": "y = 3x - 1", "d": "y = -3x + 5"}, "ans": "a"},
        {"q": "Find the equation of the line passing through (1, 3) and (3, 7).", "opts": {"a": "y = 2x + 1", "b": "y = 2x - 1", "c": "y = 4x - 1", "d": "y = x + 2"}, "ans": "a"},
        {"q": "Determine the equation of the line passing through (-2, 4) that is parallel to the line y = 3x - 5.", "opts": {"a": "y = 3x + 10", "b": "y = 3x - 10", "c": "y = -1/3x + 4", "d": "y = 3x + 4"}, "ans": "a"},
        {"q": "Determine the equation of the line passing through (3, -1) that is perpendicular to the line y = 2x + 4.", "opts": {"a": "y = -1/2x + 1/2", "b": "y = -1/2x + 1", "c": "y = 2x - 7", "d": "y = -1/2x - 5/2"}, "ans": "a"},
        {"q": "Find the distance between the point (1, 2) and the line 3x + 4y - 6 = 0.", "opts": {"a": "1", "b": "2", "c": "5", "d": "1/5"}, "ans": "a"},
        {"q": "Find the angle of inclination of the line y = x + 4.", "opts": {"a": "45°", "b": "30°", "c": "60°", "d": "90°"}, "ans": "a"},
        {"q": "Find the angle of inclination of the line y = √3x - 2.", "opts": {"a": "60°", "b": "30°", "c": "45°", "d": "90°"}, "ans": "a"},
        {"q": "Find the equation of a line with x-intercept 3 and y-intercept 4.", "opts": {"a": "4x + 3y - 12 = 0", "b": "3x + 4y - 12 = 0", "c": "4x - 3y - 12 = 0", "d": "y = 4/3x + 4"}, "ans": "a"},
        {"q": "What is the general form of the equation of a circle with center (h, k) and radius r?", "opts": {"a": "(x - h)² + (y - k)² = r²", "b": "(x + h)² + (y + k)² = r²", "c": "x² + y² = r²", "d": "(x - h)² + (y - k)² = r"}, "ans": "a"},
        {"q": "Find the equation of the circle centered at (2, -3) with a radius of 4.", "opts": {"a": "(x - 2)² + (y + 3)² = 16", "b": "(x - 2)² + (y - 3)² = 16", "c": "(x + 2)² + (y - 3)² = 16", "d": "(x - 2)² + (y + 3)² = 4"}, "ans": "a"},
        {"q": "Identify the center and radius of the circle given by the equation: x² + y² - 4x + 6y - 3 = 0.", "opts": {"a": "Center (2, -3), Radius 4", "b": "Center (-2, 3), Radius 4", "c": "Center (2, -3), Radius 16", "d": "Center (4, -6), Radius √3"}, "ans": "a"},
        {"q": "Find the slope of a line perpendicular to 3x - 4y = 12.", "opts": {"a": "-4/3", "b": "3/4", "c": "-3/4", "d": "4/3"}, "ans": "a"},
        {"q": "Find the slope of the line passing through the midpoint of (2, 4) and (6, 8), and the origin.", "opts": {"a": "3/2", "b": "2/3", "c": "1", "d": "2"}, "ans": "a"},
        {"q": "Find the distance between the parallel lines y = 2x + 3 and y = 2x - 7.", "opts": {"a": "2√5", "b": "10", "c": "√5", "d": "4"}, "ans": "a"},
        {"q": "The lines y = 3x - 2 and 3y + x = 6 are:", "opts": {"a": "perpendicular", "b": "parallel", "c": "intersecting but not perpendicular", "d": "coincident"}, "ans": "a"},
        {"q": "The lines y = 2x + 5 and 2y - 4x = 8 are:", "opts": {"a": "parallel", "b": "perpendicular", "c": "coincident", "d": "intersecting"}, "ans": "a"},
        {"q": "Find the equation of the line through (4, -3) which has a slope of 0.", "opts": {"a": "y = -3", "b": "x = 4", "c": "y = 4", "d": "x = -3"}, "ans": "a"},
        {"q": "Find the equation of the line through (4, -3) which has an undefined slope.", "opts": {"a": "x = 4", "b": "y = -3", "c": "y = 4", "d": "x = -3"}, "ans": "a"},
        {"q": "Find the equation of the line passing through (-1, 2) and perpendicular to the x-axis.", "opts": {"a": "x = -1", "b": "y = 2", "c": "x = 2", "d": "y = -1"}, "ans": "a"},
        {"q": "Find the equation of the line passing through (-1, 2) and perpendicular to the y-axis.", "opts": {"a": "y = 2", "b": "x = -1", "c": "x = 2", "d": "y = -1"}, "ans": "a"},
        {"q": "What is the value of k if the line passing through (2, 5) and (4, k) has a slope of 3?", "opts": {"a": "11", "b": "8", "c": "2", "d": "14"}, "ans": "a"},
        {"q": "What is the value of k if the line passing through (1, k) and (3, 4) is perpendicular to a line with slope -2?", "opts": {"a": "3", "b": "5", "c": "2", "d": "1"}, "ans": "a"},
        {"q": "Find the coordinates of the point that divides the segment from (1, 1) to (4, 7) in the ratio 1:2.", "opts": {"a": "(2, 3)", "b": "(2, 4)", "c": "(3, 5)", "d": "(2.5, 4)"}, "ans": "a"},
        {"q": "Find the distance of the point (-3, 4) from the y-axis.", "opts": {"a": "3", "b": "4", "c": "-3", "d": "5"}, "ans": "a"},
        {"q": "Find the distance of the point (-3, 4) from the x-axis.", "opts": {"a": "4", "b": "3", "c": "-3", "d": "5"}, "ans": "a"},
        {"q": "Find the equation of a line with inclination angle 135° and passing through the origin.", "opts": {"a": "y = -x", "b": "y = x", "c": "x + y - 1 = 0", "d": "y = √3x"}, "ans": "a"},
        {"q": "Find the equation of the perpendicular bisector of the segment joining (2, 4) and (6, 8).", "opts": {"a": "x + y - 10 = 0", "b": "x - y + 2 = 0", "c": "x + y - 6 = 0", "d": "y = x + 2"}, "ans": "a"},
        {"q": "Find the radius of the circle with equation: x² + y² - 8x - 10y + 5 = 0.", "opts": {"a": "6", "b": "36", "c": "√36", "d": "8"}, "ans": "a"},
        {"q": "What is the slope of the line tangent to the circle x² + y² = 25 at the point (3, 4)?", "opts": {"a": "-3/4", "b": "4/3", "c": "-4/3", "d": "3/4"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Find the shortest distance between the point (-2, 3) and the circle x² + y² - 4x + 6y - 12 = 0.", "opts": {"a": "5", "b": "10", "c": "0", "d": "3"}, "ans": "a"},
        {"q": "Find the coordinates of the point on the line y = 2x + 1 that is closest to the point (3, 2).", "opts": {"a": "(1.4, 3.8)", "b": "(1.5, 4.0)", "c": "(2.0, 5.0)", "d": "(1.0, 3.0)"}, "ans": "a"},
        {"q": "Find the equation of the line that is tangent to the circle (x - 1)² + (y + 2)² = 25 at the point (4, 2).", "opts": {"a": "3x + 4y - 20 = 0", "b": "4x + 3y - 22 = 0", "c": "3x - 4y - 4 = 0", "d": "3x + 4y - 12 = 0"}, "ans": "a"},
        {"q": "Find the equations of the lines passing through (0, 5) which are tangent to the circle x² + y² = 9.", "opts": {"a": "4x - 3y + 15 = 0 and 4x + 3y - 15 = 0", "b": "3x - 4y + 20 = 0 and 3x + 4y - 20 = 0", "c": "y = 3 and x = 3", "d": "4x + 3y - 15 = 0 and y = 5"}, "ans": "a"},
        {"q": "What are the coordinates of the center of a circle passing through the points (0, 0), (8, 0), and (0, 6)?", "opts": {"a": "(4, 3)", "b": "(2, 3)", "c": "(4, 2)", "d": "(3, 4)"}, "ans": "a"},
        {"q": "Find the equation of the line passing through the intersection of 2x - 3y + 4 = 0 and x + 2y - 5 = 0, and perpendicular to 3x - 4y = 7.", "opts": {"a": "28x + 21y - 65 = 0", "b": "4x + 3y - 7 = 0", "c": "4x - 3y - 1 = 0", "d": "28x - 21y + 1 = 0"}, "ans": "a"},
        {"q": "Find the distance between the point (5, 6) and the line passing through (-1, 2) and (3, -1).", "opts": {"a": "37/5", "b": "29/5", "c": "7", "d": "6.5"}, "ans": "a"},
        {"q": "Find the value of k for which the distance from (2, 3) to the line 3x - 4y + k = 0 is 2 units.", "opts": {"a": "16 or -4", "b": "10 or -10", "c": "6 or -14", "d": "12 or -8"}, "ans": "a"},
        {"q": "A line passes through (1, 2) and has its segment between the axes bisected at this point. Find its equation.", "opts": {"a": "2x + y - 4 = 0", "b": "x + 2y - 5 = 0", "c": "2x - y = 0", "d": "x + y - 3 = 0"}, "ans": "a"},
        {"q": "Determine the equation of the circle which has the segment joining (1, 2) and (5, 6) as a diameter.", "opts": {"a": "(x - 3)² + (y - 4)² = 8", "b": "(x - 3)² + (y - 4)² = 32", "c": "(x - 3)² + (y - 4)² = 16", "d": "(x - 1)² + (y - 2)² = 8"}, "ans": "a"},
        {"q": "Find the equation of the parabola with focus (2, 0) and directrix x = -2.", "opts": {"a": "y² = 8x", "b": "y² = 4x", "c": "x² = 8y", "d": "y² = -8x"}, "ans": "a"},
        {"q": "Find the coordinates of the focus of the parabola y² = -12x.", "opts": {"a": "(-3, 0)", "b": "(3, 0)", "c": "(0, -3)", "d": "(0, 3)"}, "ans": "a"},
        {"q": "Find the equation of the ellipse with vertices (±5, 0) and foci (±3, 0).", "opts": {"a": "x²/25 + y²/16 = 1", "b": "x²/16 + y²/25 = 1", "c": "x²/25 + y²/9 = 1", "d": "x²/9 + y²/25 = 1"}, "ans": "a"},
        {"q": "Find the length of the major axis of the ellipse x²/36 + y²/20 = 1.", "opts": {"a": "12", "b": "6", "c": "10", "d": "2√20"}, "ans": "a"},
        {"q": "Find the equations of the asymptotes of the hyperbola x²/9 - y²/16 = 1.", "opts": {"a": "y = ±4/3x", "b": "y = ±3/4x", "c": "y = ±16/9x", "d": "y = ±9/16x"}, "ans": "a"},
        {"q": "Find the eccentricity of the ellipse x²/25 + y²/16 = 1.", "opts": {"a": "3/5", "b": "4/5", "c": "9/25", "d": "5/3"}, "ans": "a"},
        {"q": "Find the equations of the lines parallel to 3x - 4y = 5 that are at a distance of 3 units from the origin.", "opts": {"a": "3x - 4y = ±15", "b": "3x - 4y = ±5", "c": "3x - 4y = ±3", "d": "3x - 4y = ±12"}, "ans": "a"},
        {"q": "Find the equation of the circle centered at (3, 4) and tangent to the x-axis.", "opts": {"a": "(x - 3)² + (y - 4)² = 16", "b": "(x - 3)² + (y - 4)² = 9", "c": "(x - 3)² + (y - 4)² = 25", "d": "(x - 3)² + (y - 4)² = 4"}, "ans": "a"},
        {"q": "Find the equation of the circle centered at (3, 4) and tangent to the y-axis.", "opts": {"a": "(x - 3)² + (y - 4)² = 9", "b": "(x - 3)² + (y - 4)² = 16", "c": "(x - 3)² + (y - 4)² = 25", "d": "(x - 3)² + (y - 4)² = 3"}, "ans": "a"},
        {"q": "If the circle x² + y² - kx - 4y + 3 = 0 has a radius of 2, find the value(s) of k.", "opts": {"a": "±2", "b": "±4", "c": "±√2", "d": "±3"}, "ans": "a"},
        {"q": "Find the equation of the line passing through the point of intersection of x - y - 1 = 0 and 2x - 3y + 1 = 0, and parallel to the line x + y = 0.", "opts": {"a": "x + y - 7 = 0", "b": "x + y - 5 = 0", "c": "x - y + 1 = 0", "d": "x + y - 3 = 0"}, "ans": "a"},
        {"q": "Find the coordinates of the vertices of the hyperbola y²/9 - x²/16 = 1.", "opts": {"a": "(0, ±3)", "b": "(±4, 0)", "c": "(0, ±4)", "d": "(±3, 0)"}, "ans": "a"},
        {"q": "Find the length of the latus rectum of the parabola y² = 16x.", "opts": {"a": "16", "b": "4", "c": "8", "d": "32"}, "ans": "a"},
        {"q": "Find the equation of the tangent to the parabola y² = 8x at the point (2, 4).", "opts": {"a": "x - y + 2 = 0", "b": "2x - y = 0", "c": "x + y - 6 = 0", "d": "x - 2y + 6 = 0"}, "ans": "a"},
        {"q": "Find the equation of the normal to the ellipse x²/25 + y²/9 = 1 at the point (0, 3).", "opts": {"a": "x = 0 (the y-axis)", "b": "y = 3", "c": "y = 0", "d": "x = 5"}, "ans": "a"},
        {"q": "Find the equations of the tangents to the circle x² + y² = 10 at the points where the x-coordinate is 1.", "opts": {"a": "x ± 3y - 10 = 0", "b": "x ± 3y - 1 = 0", "c": "3x ± y - 10 = 0", "d": "x ± 3y = 0"}, "ans": "a"},
        {"q": "Find the area of the triangle formed by the coordinate axes and the line 3x - 4y = 24.", "opts": {"a": "24 square units", "b": "12 square units", "c": "48 square units", "d": "6 square units"}, "ans": "a"},
        {"q": "Determine the value of m for which the line y = mx + 2 is tangent to the circle x² + y² = 1.", "opts": {"a": "±√3", "b": "±3", "c": "±√2", "d": "±1"}, "ans": "a"},
        {"q": "What is the equation of the directrix of the parabola x² = -8y?", "opts": {"a": "y = 2", "b": "y = -2", "c": "x = 2", "d": "x = -2"}, "ans": "a"},
        {"q": "Find the length of the minor axis of the ellipse 4x² + 9y² = 36.", "opts": {"a": "4", "b": "6", "c": "2", "d": "3"}, "ans": "a"},
        {"q": "Determine the eccentricity of the hyperbola x²/9 - y²/16 = 1.", "opts": {"a": "5/3", "b": "5/4", "c": "4/3", "d": "25/9"}, "ans": "a"},
        {"q": "Find the distance between the foci of the ellipse x²/100 + y²/64 = 1.", "opts": {"a": "12", "b": "6", "c": "20", "d": "16"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch3_questions():
    # Chapter 3: Geometry and Vectors
    # Focus: Vector magnitude, addition, dot product, angles in circles, triangle theorems, vectors perpendicularity.
    easy = [
        {"q": "What is the magnitude of the vector v = 3i + 4j?", "opts": {"a": "5", "b": "7", "c": "25", "d": "√7"}, "ans": "a"},
        {"q": "Given vectors a = 2i + 3j and b = 4i - j, find a + b.", "opts": {"a": "6i + 2j", "b": "6i + 4j", "c": "2i + 4j", "d": "8i - 3j"}, "ans": "a"},
        {"q": "Given vectors a = 2i + 3j and b = 4i - j, find a - b.", "opts": {"a": "-2i + 4j", "b": "-2i + 2j", "c": "2i - 4j", "d": "-6i + 4j"}, "ans": "a"},
        {"q": "What is the dot product of vectors a = (1, 3) and b = (4, 2)?", "opts": {"a": "10", "b": "7", "c": "12", "d": "14"}, "ans": "a"},
        {"q": "What is the magnitude of the unit vector?", "opts": {"a": "1", "b": "0", "c": "undefined", "d": "π"}, "ans": "a"},
        {"q": "Find the magnitude of the vector w = -6i + 8j.", "opts": {"a": "10", "b": "14", "c": "-2", "d": "100"}, "ans": "a"},
        {"q": "If vector a = 3i - 2j, find the scalar product 2a.", "opts": {"a": "6i - 4j", "b": "6i - 2j", "c": "5i - 4j", "d": "6i + 4j"}, "ans": "a"},
        {"q": "What is the sum of angles in a triangle?", "opts": {"a": "180 degrees", "b": "360 degrees", "c": "90 degrees", "d": "270 degrees"}, "ans": "a"},
        {"q": "What is the sum of angles in a quadrilateral?", "opts": {"a": "360 degrees", "b": "180 degrees", "c": "540 degrees", "d": "90 degrees"}, "ans": "a"},
        {"q": "An angle subtended by a semicircle diameter at any point on the boundary is:", "opts": {"a": "90 degrees (right angle)", "b": "180 degrees", "c": "45 degrees", "d": "60 degrees"}, "ans": "a"},
        {"q": "If two vectors are perpendicular, their dot product is:", "opts": {"a": "0", "b": "1", "c": "-1", "d": "undefined"}, "ans": "a"},
        {"q": "If the dot product of two vectors is 0, the vectors are:", "opts": {"a": "perpendicular", "b": "parallel", "c": "equal", "d": "opposite"}, "ans": "a"},
        {"q": "Find the magnitude of the vector u = (5, 12).", "opts": {"a": "13", "b": "17", "c": "7", "d": "√17"}, "ans": "a"},
        {"q": "If vector v = (2, -3), find -3v.", "opts": {"a": "(-6, 9)", "b": "(-6, -9)", "c": "(6, -9)", "d": "(-1, -6)"}, "ans": "a"},
        {"q": "What is the dot product of vectors i and j?", "opts": {"a": "0", "b": "1", "c": "-1", "d": "undefined"}, "ans": "a"},
        {"q": "What is the dot product of vector i with itself?", "opts": {"a": "1", "b": "0", "c": "-1", "d": "2"}, "ans": "a"},
        {"q": "What is the dot product of vector j with itself?", "opts": {"a": "1", "b": "0", "c": "-1", "d": "2"}, "ans": "a"},
        {"q": "What is a polygon with 5 sides called?", "opts": {"a": "Pentagon", "b": "Hexagon", "c": "Heptagon", "d": "Octagon"}, "ans": "a"},
        {"q": "What is a polygon with 6 sides called?", "opts": {"a": "Hexagon", "b": "Pentagon", "c": "Octagon", "d": "Decagon"}, "ans": "a"},
        {"q": "The exterior angles of any convex polygon always sum to:", "opts": {"a": "360 degrees", "b": "180 degrees", "c": "540 degrees", "d": "720 degrees"}, "ans": "a"},
        {"q": "Find the dot product of a = 2i + 5j and b = 3i - 2j.", "opts": {"a": "-4", "b": "16", "c": "11", "d": "6"}, "ans": "a"},
        {"q": "If the magnitude of a vector is 1, it is called a _____ vector.", "opts": {"a": "unit", "b": "zero", "c": "scalar", "d": "equal"}, "ans": "a"},
        {"q": "What is the sum of the interior angles of a pentagon?", "opts": {"a": "540 degrees", "b": "360 degrees", "c": "720 degrees", "d": "180 degrees"}, "ans": "a"},
        {"q": "Find the magnitude of the vector (1, 1).", "opts": {"a": "√2", "b": "2", "c": "1", "d": "0"}, "ans": "a"},
        {"q": "Find the dot product of vectors (2, 0) and (0, -5).", "opts": {"a": "0", "b": "-10", "c": "2", "d": "-5"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "Find the cosine of the angle between vectors a = (3, 4) and b = (5, 12).", "opts": {"a": "63/65", "b": "33/65", "c": "56/65", "d": "16/65"}, "ans": "a"},
        {"q": "Find the value of k for which vectors a = 2i + kj and b = 3i - 6j are perpendicular.", "opts": {"a": "1", "b": "-1", "c": "2", "d": "-2"}, "ans": "a"},
        {"q": "If vectors a = (1, 2) and b = (k, 6) are parallel, find the value of k.", "opts": {"a": "3", "b": "2", "c": "1/3", "d": "12"}, "ans": "a"},
        {"q": "Find the projection of vector a = (2, 3) onto vector b = (4, 0).", "opts": {"a": "(2, 0)", "b": "(4, 0)", "c": "(0, 3)", "d": "(2, 3)"}, "ans": "a"},
        {"q": "What is the interior angle of a regular hexagon?", "opts": {"a": "120 degrees", "b": "108 degrees", "c": "135 degrees", "d": "90 degrees"}, "ans": "a"},
        {"q": "What is the interior angle of a regular octagon?", "opts": {"a": "135 degrees", "b": "120 degrees", "c": "108 degrees", "d": "140 degrees"}, "ans": "a"},
        {"q": "The angles of a triangle are in the ratio 2:3:5. Find the measure of the smallest angle.", "opts": {"a": "36°", "b": "18°", "c": "54°", "d": "90°"}, "ans": "a"},
        {"q": "In a circle with center O, if arc AB subtends an angle of 80° at the center, what angle does it subtend at the circumference?", "opts": {"a": "40°", "b": "80°", "c": "160°", "d": "20°"}, "ans": "a"},
        {"q": "What is the equation of the vector passing through (1, 2) in the direction of vector (3, 4)?", "opts": {"a": "r = (1, 2) + t(3, 4)", "b": "r = (3, 4) + t(1, 2)", "c": "r = (1, 3) + t(2, 4)", "d": "r = t(3, 4)"}, "ans": "a"},
        {"q": "Find the unit vector in the direction of v = (8, -6).", "opts": {"a": "(0.8, -0.6)", "b": "(0.6, -0.8)", "c": "(8, -6)", "d": "(1, 1)"}, "ans": "a"},
        {"q": "Calculate the dot product: (2i - 3j) * (4i + 5j).", "opts": {"a": "-7", "b": "8", "c": "-15", "d": "23"}, "ans": "a"},
        {"q": "Find the angle between the vectors i + j and i - j.", "opts": {"a": "90°", "b": "0°", "c": "45°", "d": "180°"}, "ans": "a"},
        {"q": "If the interior angles of a polygon sum to 900 degrees, how many sides does the polygon have?", "opts": {"a": "7", "b": "6", "c": "8", "d": "9"}, "ans": "a"},
        {"q": "In a cyclic quadrilateral, the opposite angles always sum to:", "opts": {"a": "180 degrees", "b": "360 degrees", "c": "90 degrees", "d": "270 degrees"}, "ans": "a"},
        {"q": "A tangent to a circle is _____ to the radius at the point of contact.", "opts": {"a": "perpendicular", "b": "parallel", "c": "equal", "d": "complementary"}, "ans": "a"},
        {"q": "If arc CD subtends an angle of 35° at the circumference, find the angle it subtends at the center of the circle.", "opts": {"a": "70°", "b": "35°", "c": "17.5°", "d": "140°"}, "ans": "a"},
        {"q": "Find the magnitude of the vector sum a + b if a = (3, 1) and b = (1, 2).", "opts": {"a": "5", "b": "25", "c": "7", "d": "√7"}, "ans": "a"},
        {"q": "Find the value of x if the interior angle of a regular polygon is 144°. How many sides does it have?", "opts": {"a": "10", "b": "8", "c": "12", "d": "6"}, "ans": "a"},
        {"q": "Given vectors u = 3i - j and v = i + 2j, find the magnitude of 2u - v.", "opts": {"a": "√41", "b": "√29", "c": "5", "d": "√17"}, "ans": "a"},
        {"q": "Find the scalar k such that |k * (3i + 4j)| = 15.", "opts": {"a": "±3", "b": "±5", "c": "±15", "d": "±1"}, "ans": "a"},
        {"q": "If the dot product of a and b is negative, the angle between them is:", "opts": {"a": "obtuse (between 90° and 180°)", "b": "acute (between 0° and 90°)", "c": "right angle (90°)", "d": "straight angle (180°)"}, "ans": "a"},
        {"q": "If the dot product of a and b is positive, the angle between them is:", "opts": {"a": "acute (between 0° and 90°)", "b": "obtuse (between 90° and 180°)", "c": "right angle (90°)", "d": "straight angle (180°)"}, "ans": "a"},
        {"q": "State the Midpoint Theorem for triangles.", "opts": {"a": "The line segment connecting midpoints of two sides is parallel to the third side and half its length", "b": "The area of the triangle is halved by any midpoint line segment", "c": "The line connects the vertex to the opposite side's midpoint perpendicularly", "d": "The midpoints form an equilateral triangle"}, "ans": "a"},
        {"q": "In an isosceles triangle, the angles opposite to the equal sides are:", "opts": {"a": "equal", "b": "complementary", "c": "supplementary", "d": "obtuse"}, "ans": "a"},
        {"q": "Find the projection of vector (3, 4) onto vector i.", "opts": {"a": "3i", "b": "4i", "c": "3", "d": "4"}, "ans": "a"},
        {"q": "Find the projection of vector (3, 4) onto vector j.", "opts": {"a": "4j", "b": "3j", "c": "4", "d": "3"}, "ans": "a"},
        {"q": "If vectors a = (2, -3) and b = (x, 4) are perpendicular, find x.", "opts": {"a": "6", "b": "-6", "c": "8", "d": "-8"}, "ans": "a"},
        {"q": "Find the distance between vectors a = (1, 2) and b = (4, 6).", "opts": {"a": "5", "b": "25", "c": "7", "d": "√7"}, "ans": "a"},
        {"q": "If cyclic quadrilateral ABCD has angle A = 110°, find angle C.", "opts": {"a": "70°", "b": "110°", "c": "180°", "d": "90°"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Find the angle between vectors a = i + √3j and b = √3i + j.", "opts": {"a": "30°", "b": "60°", "c": "45°", "d": "90°"}, "ans": "a"},
        {"q": "If vector a = (x, 2) and b = (1, 3) are such that the angle between them is 45°, find the value(s) of x.", "opts": {"a": "1 or -1/7 (Wait, 8 or -1/2)", "b": "1 or 7", "c": "2 or -3", "d": "8 or -1"}, "ans": "a"},
        {"q": "Prove that the vector a = (x, y) is perpendicular to b = (-y, x). Find their dot product.", "opts": {"a": "0 (since -xy + yx = 0)", "b": "x² + y²", "c": "-xy", "d": "1"}, "ans": "a"},
        {"q": "Find the vector equation of the line passing through points A(1, 3, 2) and B(4, 5, 0) in 3D space.", "opts": {"a": "r = (1, 3, 2) + t(3, 2, -2)", "b": "r = (3, 2, -2) + t(1, 3, 2)", "c": "r = (1, 3, 2) + t(4, 5, 0)", "d": "r = (5, 8, 2) + t(3, 2, -2)"}, "ans": "a"},
        {"q": "Given vectors a = i - 2j + 2k and b = 3i - 6j + 2k, find the angle between them.", "opts": {"a": "arccos(19/21)", "b": "arccos(15/21)", "c": "arccos(17/21)", "d": "90°"}, "ans": "a"},
        {"q": "Calculate the area of a triangle with vertices at vector coordinates A(0,0,0), B(1,2,0), and C(0,3,1) using cross product.", "opts": {"a": "√14/2", "b": "√14", "c": "√10/2", "d": "5"}, "ans": "a"},
        {"q": "A chord AB of a circle has length 8 cm, and the radius of the circle is 5 cm. Find the distance of the chord from the center O.", "opts": {"a": "3 cm", "b": "4 cm", "c": "√9", "d": "2.5 cm"}, "ans": "a"},
        {"q": "Two tangents PA and PB are drawn to a circle with center O from an external point P. If angle APB = 60°, find angle AOB.", "opts": {"a": "120°", "b": "60°", "c": "90°", "d": "150°"}, "ans": "a"},
        {"q": "State the Alternating Segment Theorem for circles.", "opts": {"a": "The angle between a tangent and a chord through the point of contact is equal to the angle in the alternate segment", "b": "The tangents from an external point are equal in length", "c": "Opposite angles of a cyclic quadrilateral sum to 180°", "d": "The radius is perpendicular to the tangent at contact"}, "ans": "a"},
        {"q": "Find the value of scalar m if vectors a = mi + 2j - k and b = 3i - j + mk are perpendicular.", "opts": {"a": "1", "b": "-1", "c": "2", "d": "-2"}, "ans": "a"},
        {"q": "Find the unit vector perpendicular to both a = (1, 1, 0) and b = (0, 1, 1).", "opts": {"a": "(1/√3, -1/√3, 1/√3)", "b": "(1/√2, 0, -1/√2)", "c": "(1, -1, 1)", "d": "(0, 0, 1)"}, "ans": "a"},
        {"q": "Evaluate the magnitude of the vector cross product a x b where a = (2, 3, 0) and b = (1, -1, 0).", "opts": {"a": "5", "b": "5k", "c": "1", "d": "√13"}, "ans": "a"},
        {"q": "Find the value of interior angle sum of a decagon.", "opts": {"a": "1440 degrees", "b": "1080 degrees", "c": "1260 degrees", "d": "1620 degrees"}, "ans": "a"},
        {"q": "If the coordinates of the vertices of a triangle are A(1, 1), B(5, 1), and C(1, 4), find the perimeter of the triangle.", "opts": {"a": "12", "b": "10", "c": "7 + √7", "d": "14"}, "ans": "a"},
        {"q": "Find the area of the triangle with vertices A(1, 1), B(5, 1), and C(1, 4).", "opts": {"a": "6 square units", "b": "12 square units", "c": "8 square units", "d": "10 square units"}, "ans": "a"},
        {"q": "What is the vector equation of the plane passing through (1, 2, 3) and perpendicular to the vector 2i - j + 2k?", "opts": {"a": "2x - y + 2z - 6 = 0", "b": "2x - y + 2z - 3 = 0", "c": "x + 2y + 3z - 6 = 0", "d": "2x - y + 2z = 0"}, "ans": "a"},
        {"q": "Find the direction cosines of the vector v = i + 2j + 2k.", "opts": {"a": "1/3, 2/3, 2/3", "b": "1, 2, 2", "c": "1/√5, 2/√5, 0", "d": "1/9, 2/9, 2/9"}, "ans": "a"},
        {"q": "Find the volume of the parallelepiped determined by vectors a=(1,0,0), b=(0,2,0), and c=(1,1,3) using triple scalar product.", "opts": {"a": "6", "b": "3", "c": "5", "d": "2"}, "ans": "a"},
        {"q": "If P divides AB in the ratio 2:3, and the coordinates are A(1, 2) and B(6, 7), find P.", "opts": {"a": "(3, 4)", "b": "(4, 5)", "c": "(2.5, 3.5)", "d": "(3.5, 4.5)"}, "ans": "a"},
        {"q": "If the angle of inclination of a line is 60°, find the slope of a line perpendicular to it.", "opts": {"a": "-1/√3", "b": "√3", "c": "-√3", "d": "1/2"}, "ans": "a"},
        {"q": "In circle geometry, if cyclic quad ABCD has angle B = 2x + 10° and angle D = 3x - 20°, find x.", "opts": {"a": "38°", "b": "30°", "c": "40°", "d": "35°"}, "ans": "a"},
        {"q": "Given vectors a = 3i + 4j and b = 5i - 12j, calculate the dot product of a + b and a - b.", "opts": {"a": "-119", "b": "119", "c": "25 - 169", "d": "0"}, "ans": "a"},
        {"q": "What is the cosine of the angle between vectors (1, 2, 2) and (2, 2, 1)?", "opts": {"a": "8/9", "b": "7/9", "c": "2/3", "d": "1"}, "ans": "a"},
        {"q": "If a triangle has sides of length 8 cm, 15 cm, and 17 cm, the triangle is:", "opts": {"a": "right-angled", "b": "acute-angled", "c": "obtuse-angled", "d": "equilateral"}, "ans": "a"},
        {"q": "If the vectors a = (k, 3, -1) and b = (2, -k, 5) are perpendicular, solve for k.", "opts": {"a": "-5", "b": "5", "c": "2", "d": "-2"}, "ans": "a"},
        {"q": "Find the cross product of a = (1, 0, 0) and b = (0, 1, 0).", "opts": {"a": "(0, 0, 1)", "b": "(0, 1, 0)", "c": "(1, 0, 0)", "d": "(0, 0, 0)"}, "ans": "a"},
        {"q": "Find the distance from the point (1, 1, 1) to the plane x + 2y + 2z - 11 = 0.", "opts": {"a": "2", "b": "3", "c": "6/3", "d": "5"}, "ans": "a"},
        {"q": "In a cyclic quad ABCD, if diagonals intersect at P such that AP * PC = BP * PD. This is a property of:", "opts": {"a": "intersecting chords theorem", "b": "tangent-secant theorem", "c": "cyclic quadrilateral angles", "d": "midpoint theorem"}, "ans": "a"},
        {"q": "If the interior angle of a regular polygon is 150°, find the number of sides.", "opts": {"a": "12", "b": "10", "c": "8", "d": "6"}, "ans": "a"},
        {"q": "Find the vector perpendicular to both (2, 1) and (-1, 3) in the 2D plane.", "opts": {"a": "There is no 2D vector perpendicular to both non-parallel vectors", "b": "(1, -2)", "c": "(3, 1)", "d": "(0, 0)"}, "ans": "a"},
        {"q": "If the magnitude of vector cross product |a x b| = a * b, what is the angle between them?", "opts": {"a": "45°", "b": "90°", "c": "0°", "d": "180°"}, "ans": "a"},
        {"q": "Find the dot product: (i + 2j + 3k) * (3i - 2j + k).", "opts": {"a": "2", "b": "4", "c": "6", "d": "0"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch4_questions():
    # Chapter 4: Probability
    # Focus: Combined events, mutually exclusive events, independent events, tree diagrams.
    easy = [
        {"q": "What is the probability of an event that is certain to happen?", "opts": {"a": "1", "b": "0", "c": "0.5", "d": "undefined"}, "ans": "a"},
        {"q": "What is the probability of an impossible event?", "opts": {"a": "0", "b": "1", "c": "-1", "d": "0.5"}, "ans": "a"},
        {"q": "If the probability of it raining tomorrow is 0.3, what is the probability of it not raining?", "opts": {"a": "0.7", "b": "0.3", "c": "0.5", "d": "0.4"}, "ans": "a"},
        {"q": "A fair six-sided die is rolled. What is the probability of rolling a 4?", "opts": {"a": "1/6", "b": "1/2", "c": "2/3", "d": "1/3"}, "ans": "a"},
        {"q": "A coin is tossed. What is the probability of getting heads?", "opts": {"a": "1/2", "b": "1", "c": "0", "d": "1/4"}, "ans": "a"},
        {"q": "What is the range of values for any probability P(A)?", "opts": {"a": "0 ≤ P(A) ≤ 1", "b": "-1 ≤ P(A) ≤ 1", "c": "0 < P(A) < 1", "d": "P(A) ≥ 0"}, "ans": "a"},
        {"q": "A card is drawn from a standard deck of 52 cards. How many suits are in the deck?", "opts": {"a": "4", "b": "13", "c": "2", "d": "26"}, "ans": "a"},
        {"q": "How many red cards are in a standard deck of 52 playing cards?", "opts": {"a": "26", "b": "13", "c": "4", "d": "52"}, "ans": "a"},
        {"q": "How many face cards (Jack, Queen, King) are in a standard 52-card deck?", "opts": {"a": "12", "b": "4", "c": "8", "d": "16"}, "ans": "a"},
        {"q": "If two events A and B cannot happen at the same time, they are said to be:", "opts": {"a": "mutually exclusive", "b": "independent", "c": "dependent", "d": "complementary"}, "ans": "a"},
        {"q": "If rolling a die does not affect the outcome of tossing a coin, the events are:", "opts": {"a": "independent", "b": "mutually exclusive", "c": "dependent", "d": "coincident"}, "ans": "a"},
        {"q": "A bag contains 3 red balls and 7 blue balls. What is the probability of drawing a red ball?", "opts": {"a": "3/10", "b": "7/10", "c": "3/7", "d": "1/3"}, "ans": "a"},
        {"q": "A bag contains 3 red balls and 7 blue balls. What is the probability of drawing a blue ball?", "opts": {"a": "7/10", "b": "3/10", "c": "7/3", "d": "2/3"}, "ans": "a"},
        {"q": "A fair six-sided die is rolled. What is the probability of rolling an even number?", "opts": {"a": "1/2", "b": "1/3", "c": "2/3", "d": "1/6"}, "ans": "a"},
        {"q": "A fair six-sided die is rolled. What is the probability of rolling an odd number?", "opts": {"a": "1/2", "b": "1/3", "c": "2/3", "d": "1/6"}, "ans": "a"},
        {"q": "What is the probability of rolling a number greater than 4 on a fair six-sided die?", "opts": {"a": "1/3", "b": "1/2", "c": "2/3", "d": "1/6"}, "ans": "a"},
        {"q": "If P(A) = 0.4 and P(B) = 0.5, and A and B are mutually exclusive, find P(A or B).", "opts": {"a": "0.9", "b": "0.2", "c": "0.1", "d": "0.5"}, "ans": "a"},
        {"q": "What is the probability of drawing an Ace from a standard deck of 52 cards?", "opts": {"a": "1/13", "b": "1/52", "c": "4/13", "d": "1/4"}, "ans": "a"},
        {"q": "What is the sum of probabilities of all possible outcomes in a sample space?", "opts": {"a": "1", "b": "100", "c": "0.5", "d": "0"}, "ans": "a"},
        {"q": "Tossing two coins. What is the size of the sample space?", "opts": {"a": "4", "b": "2", "c": "8", "d": "6"}, "ans": "a"},
        {"q": "Tossing three coins. What is the size of the sample space?", "opts": {"a": "8", "b": "6", "c": "4", "d": "12"}, "ans": "a"},
        {"q": "Rolling two six-sided dice. What is the size of the sample space?", "opts": {"a": "36", "b": "12", "c": "18", "d": "24"}, "ans": "a"},
        {"q": "If P(A) = 0.25, what is P(A') (the complement of A)?", "opts": {"a": "0.75", "b": "0.25", "c": "0.50", "d": "-0.25"}, "ans": "a"},
        {"q": "Which of these cannot be a probability value?", "opts": {"a": "1.2", "b": "0.5", "c": "0.01", "d": "0"}, "ans": "a"},
        {"q": "A letter is chosen at random from the word 'SOMALIA'. What is the probability it is an 'A'?", "opts": {"a": "2/7", "b": "1/7", "c": "3/7", "d": "2/5"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "If P(A) = 0.3, P(B) = 0.4, and A and B are independent events, find P(A and B).", "opts": {"a": "0.12", "b": "0.7", "c": "0.1", "d": "0.5"}, "ans": "a"},
        {"q": "If P(A) = 0.3, P(B) = 0.4, and A and B are independent events, find P(A or B).", "opts": {"a": "0.58", "b": "0.70", "c": "0.12", "d": "0.82"}, "ans": "a"},
        {"q": "A box contains 5 red, 3 green, and 2 blue marbles. Two marbles are drawn one after another without replacement. Find the probability that both are red.", "opts": {"a": "2/9", "b": "1/4", "c": "5/18", "d": "1/3"}, "ans": "a"},
        {"q": "A box contains 5 red, 3 green, and 2 blue marbles. Two marbles are drawn with replacement. Find the probability that both are red.", "opts": {"a": "1/4", "b": "2/9", "c": "5/18", "d": "1/3"}, "ans": "a"},
        {"q": "Two fair dice are rolled. What is the probability that the sum of the numbers is 7?", "opts": {"a": "1/6", "b": "5/36", "c": "7/36", "d": "1/12"}, "ans": "a"},
        {"q": "Two fair dice are rolled. What is the probability that the sum of the numbers is 11?", "opts": {"a": "1/18", "b": "1/12", "c": "1/36", "d": "1/9"}, "ans": "a"},
        {"q": "What is the probability of drawing a red face card from a standard deck of 52 cards?", "opts": {"a": "3/26", "b": "3/13", "c": "6/13", "d": "1/26"}, "ans": "a"},
        {"q": "A committee of 3 people is to be chosen from a group of 5 men and 4 women. In how many ways can this committee be formed?", "opts": {"a": "84", "b": "60", "c": "24", "d": "120"}, "ans": "a"},
        {"q": "Find the number of permutations of the letters in the word 'MATHS'.", "opts": {"a": "120", "b": "60", "c": "24", "d": "720"}, "ans": "a"},
        {"q": "Find the number of distinct permutations of the letters in the word 'SOMALIA'.", "opts": {"a": "2520", "b": "5040", "c": "720", "d": "1260"}, "ans": "a"},
        {"q": "If P(A) = 0.6, P(B) = 0.5, and P(A or B) = 0.8, find P(A and B).", "opts": {"a": "0.3", "b": "0.2", "c": "0.4", "d": "0.5"}, "ans": "a"},
        {"q": "If P(A|B) = 0.4 and P(B) = 0.5, find P(A and B).", "opts": {"a": "0.2", "b": "0.8", "c": "0.1", "d": "0.25"}, "ans": "a"},
        {"q": "Two cards are drawn from a standard deck of 52 cards without replacement. What is the probability that both are Aces?", "opts": {"a": "1/221", "b": "1/169", "c": "1/26", "d": "4/663"}, "ans": "a"},
        {"q": "What is the probability of rolling a total of 12 when rolling two fair dice?", "opts": {"a": "1/36", "b": "1/18", "c": "1/12", "d": "0"}, "ans": "a"},
        {"q": "What is the probability of rolling a total of 2 when rolling two fair dice?", "opts": {"a": "1/36", "b": "1/18", "c": "1/12", "d": "1/6"}, "ans": "a"},
        {"q": "A student answers a multiple-choice exam with 5 questions, each with 4 options. If they guess randomly, what is the probability of getting all questions correct?", "opts": {"a": "1/1024", "b": "1/256", "c": "1/625", "d": "1/5"}, "ans": "a"},
        {"q": "What is the probability of drawing a spade or a King from a standard deck of 52 cards?", "opts": {"a": "4/13", "b": "17/52", "c": "9/26", "d": "1/4"}, "ans": "a"},
        {"q": "A coin is tossed three times. What is the probability of getting exactly two heads?", "opts": {"a": "3/8", "b": "1/2", "c": "1/4", "d": "5/8"}, "ans": "a"},
        {"q": "A coin is tossed three times. What is the probability of getting at least two heads?", "opts": {"a": "1/2", "b": "3/8", "c": "5/8", "d": "7/8"}, "ans": "a"},
        {"q": "In a group of 30 students, 18 play football, 12 play basketball, and 5 play both. What is the probability that a randomly chosen student plays neither?", "opts": {"a": "1/6", "b": "5/30", "c": "7/30", "d": "1/5"}, "ans": "a"},
        {"q": "What is the value of 5C3 (5 choose 3)?", "opts": {"a": "10", "b": "20", "c": "60", "d": "5"}, "ans": "a"},
        {"q": "What is the value of 6P2 (permutations of 6 items taken 2 at a time)?", "opts": {"a": "30", "b": "15", "c": "12", "d": "360"}, "ans": "a"},
        {"q": "Three light bulbs are selected from a pack containing 2 bad bulbs and 8 good bulbs. Find the probability that all three are good (without replacement).", "opts": {"a": "7/15", "b": "8/15", "c": "14/15", "d": "28/45"}, "ans": "a"},
        {"q": "If P(A) = 0.5 and P(B) = 0.3, and A and B are independent, find P(A' and B').", "opts": {"a": "0.35", "b": "0.15", "c": "0.80", "d": "0.50"}, "ans": "a"},
        {"q": "If P(A) = 0.7, what is the odds in favor of event A happening?", "opts": {"a": "7:3", "b": "3:7", "c": "7:10", "d": "10:7"}, "ans": "a"},
        {"q": "If the odds against an event are 4:5, what is the probability of the event happening?", "opts": {"a": "5/9", "b": "4/9", "c": "4/5", "d": "5/4"}, "ans": "a"},
        {"q": "A card is drawn from a deck. Find the probability that it is a red card and a Queen.", "opts": {"a": "1/26", "b": "1/13", "c": "1/52", "d": "2/13"}, "ans": "a"},
        {"q": "If P(A) = 0.4, P(B) = 0.5, and P(A and B) = 0.2, find P(A|B).", "opts": {"a": "0.4", "b": "0.5", "c": "0.2", "d": "0.8"}, "ans": "a"},
        {"q": "If P(A) = 0.4, P(B) = 0.5, and P(A and B) = 0.2, find P(B|A).", "opts": {"a": "0.5", "b": "0.4", "c": "0.2", "d": "0.8"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "A disease affects 1 in 1000 people. A test for this disease has a 99% true positive rate and a 5% false positive rate. If a person tests positive, what is the probability they actually have the disease?", "opts": {"a": "0.019 (approx 2%)", "b": "0.99 (99%)", "c": "0.95 (95%)", "d": "0.05 (5%)"}, "ans": "a"},
        {"q": "Three cards are drawn from a standard 52-card deck without replacement. What is the probability of getting a flush (three cards of the same suit)?", "opts": {"a": "22/425", "b": "11/850", "c": "1/17", "d": "13/20400"}, "ans": "a"},
        {"q": "Solve for n: nC2 = 45.", "opts": {"a": "10", "b": "9", "c": "11", "d": "45"}, "ans": "a"},
        {"q": "Solve for n: nP3 = 120.", "opts": {"a": "6", "b": "5", "c": "7", "d": "10"}, "ans": "a"},
        {"q": "A bag contains 4 red and 6 black balls. Three balls are drawn at random without replacement. What is the probability of getting at least two black balls?", "opts": {"a": "2/3", "b": "1/2", "c": "3/5", "d": "7/10"}, "ans": "a"},
        {"q": "In a binomial distribution with n = 4 and p = 0.5, find the probability of obtaining exactly 3 successes.", "opts": {"a": "0.25", "b": "0.375", "c": "0.125", "d": "0.5"}, "ans": "a"},
        {"q": "In a binomial distribution with n = 5 and p = 0.2, find the probability of obtaining at least 1 success.", "opts": {"a": "0.67232", "b": "0.32768", "c": "0.40960", "d": "0.75"}, "ans": "a"},
        {"q": "An urn contains 6 white and 4 black balls. If 2 balls are drawn without replacement, find the probability that the second ball drawn is black, given that the first was white.", "opts": {"a": "4/9", "b": "4/10", "c": "3/9", "d": "6/9"}, "ans": "a"},
        {"q": "A fair coin is tossed until a head appears. What is the probability that it takes exactly 4 tosses?", "opts": {"a": "1/16", "b": "1/8", "c": "1/32", "d": "15/16"}, "ans": "a"},
        {"q": "Two events A and B are such that P(A) = 0.5, P(B) = 0.6, and P(A' and B') = 0.1. Find P(A|B).", "opts": {"a": "1/3", "b": "2/3", "c": "1/2", "d": "4/5"}, "ans": "a"},
        {"q": "If P(A) = 0.7, P(B) = 0.4, and P(A and B) = 0.3, find P(A'|B').", "opts": {"a": "1/3", "b": "2/3", "c": "1/2", "d": "0.2"}, "ans": "a"},
        {"q": "How many words can be formed by rearranging the letters in the word 'DIFERENSHEEL' (Differentiation)?", "opts": {"a": "12! / (3! * 2!)", "b": "12!", "c": "12! / 3!", "d": "12! / (3! * 2! * 2!)"}, "ans": "a"},
        {"q": "A pair of fair dice is thrown. If the two numbers turned up are different, find the probability that the sum is 6.", "opts": {"a": "2/15", "b": "5/36", "c": "4/36", "d": "1/9"}, "ans": "a"},
        {"q": "In a certain town, 40% of people have brown hair, 25% have brown eyes, and 15% have both. Find the probability that a person chosen at random has neither brown hair nor brown eyes.", "opts": {"a": "0.50", "b": "0.65", "c": "0.35", "d": "0.45"}, "ans": "a"},
        {"q": "A committee of 4 is to be chosen from a pool of 6 men and 5 women. Find the probability that the committee contains exactly 2 men and 2 women.", "opts": {"a": "150/330", "b": "15/33", "c": "150/495", "d": "60/165"}, "ans": "a"},
        {"q": "If the probability of a target being hit is 1/3, what is the minimum number of shots required so that the probability of hitting the target at least once is greater than 0.9?", "opts": {"a": "6", "b": "5", "c": "4", "d": "7"}, "ans": "a"},
        {"q": "Three cards are drawn from a deck. Find the probability of drawing three cards of different suits.", "opts": {"a": "169/425", "b": "169/850", "c": "13/102", "d": "13/17"}, "ans": "a"},
        {"q": "State Bayes' Theorem mathematically.", "opts": {"a": "P(A|B) = P(B|A)*P(A) / P(B)", "b": "P(A|B) = P(A|B)*P(B) / P(A)", "c": "P(A and B) = P(A) * P(B)", "d": "P(A or B) = P(A) + P(B)"}, "ans": "a"},
        {"q": "A box has 10 coins, where 3 are double-headed and 7 are fair. A coin is chosen at random and tossed twice. If it lands heads twice, find the probability that it was a double-headed coin.", "opts": {"a": "12/19", "b": "3/10", "c": "12/40", "d": "3/19"}, "ans": "a"},
        {"q": "Find the number of ways to arrange 5 students in a circle.", "opts": {"a": "24", "b": "120", "c": "60", "d": "720"}, "ans": "a"},
        {"q": "Find the number of ways to arrange 6 keys on a key ring.", "opts": {"a": "60", "b": "120", "c": "720", "d": "360"}, "ans": "a"},
        {"q": "Solve for n: (n+1)! / n! = 12.", "opts": {"a": "11", "b": "12", "c": "10", "d": "13"}, "ans": "a"},
        {"q": "A bag contains 5 white and 3 black balls. If two balls are drawn at random without replacement, find the probability that they are of different colors.", "opts": {"a": "15/28", "b": "15/56", "c": "13/28", "d": "30/56"}, "ans": "a"},
        {"q": "What is the probability of rolling a total sum of 9 when rolling two fair dice?", "opts": {"a": "4/36", "b": "5/36", "c": "3/36", "d": "1/12"}, "ans": "a"},
        {"q": "Find the coefficient of the x³ term in the expansion of (x + 2)^5.", "opts": {"a": "40", "b": "10", "c": "20", "d": "80"}, "ans": "a"},
        {"q": "A test has 10 true/false questions. What is the probability of getting at least 8 correct by guessing?", "opts": {"a": "7/128", "b": "11/1024", "c": "37/1024", "d": "7/256"}, "ans": "a"},
        {"q": "If P(A) = 0.5, P(B) = 0.4, and P(A and B) = 0.1, find P(A|B').", "opts": {"a": "2/3", "b": "1/2", "c": "4/5", "d": "1/3"}, "ans": "a"},
        {"q": "Find the probability of rolling three dice and getting a sum of 4.", "opts": {"a": "3/216", "b": "4/216", "c": "1/216", "d": "2/216"}, "ans": "a"},
        {"q": "An exam consists of 8 questions, and students must answer 5. How many choices of questions does a student have?", "opts": {"a": "56", "b": "120", "c": "40", "d": "336"}, "ans": "a"},
        {"q": "If 4 coins are tossed, find the probability of getting exactly 2 heads.", "opts": {"a": "3/8", "b": "1/2", "c": "1/4", "d": "5/8"}, "ans": "a"},
        {"q": "Solve for n: nC(n-2) = 15.", "opts": {"a": "6", "b": "5", "c": "7", "d": "15"}, "ans": "a"},
        {"q": "If P(A) = 0.8 and P(B) = 0.5, find the minimum possible value of P(A and B).", "opts": {"a": "0.3", "b": "0", "c": "0.5", "d": "0.4"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch5_questions():
    # Chapter 5: Complex Numbers
    # Focus: Real/imaginary parts, conjugates, modulus, addition, subtraction, multiplication, division, polar form.
    easy = [
        {"q": "What is the value of i² in complex numbers?", "opts": {"a": "-1", "b": "1", "c": "√-1", "d": "0"}, "ans": "a"},
        {"q": "Given the complex number z = 3 + 4i, what is the real part of z?", "opts": {"a": "3", "b": "4", "c": "3 + 4i", "d": "4i"}, "ans": "a"},
        {"q": "Given the complex number z = 3 + 4i, what is the imaginary part of z?", "opts": {"a": "4", "b": "3", "c": "4i", "d": "i"}, "ans": "a"},
        {"q": "What is the conjugate of the complex number z = 2 + 3i?", "opts": {"a": "2 - 3i", "b": "-2 + 3i", "c": "-2 - 3i", "d": "3 + 2i"}, "ans": "a"},
        {"q": "What is the conjugate of the complex number z = 5 - 2i?", "opts": {"a": "5 + 2i", "b": "-5 - 2i", "c": "-5 + 2i", "d": "2 - 5i"}, "ans": "a"},
        {"q": "Perform the addition: (2 + 3i) + (4 + 5i).", "opts": {"a": "6 + 8i", "b": "8 + 6i", "c": "6 - 2i", "d": "2 + 2i"}, "ans": "a"},
        {"q": "Perform the subtraction: (7 + 5i) - (3 + 2i).", "opts": {"a": "4 + 3i", "b": "10 + 7i", "c": "4 - 3i", "d": "4 + 7i"}, "ans": "a"},
        {"q": "What is the modulus of the complex number z = 3 + 4i?", "opts": {"a": "5", "b": "25", "c": "7", "d": "√7"}, "ans": "a"},
        {"q": "What is the value of i³?", "opts": {"a": "-i", "b": "i", "c": "-1", "d": "1"}, "ans": "a"},
        {"q": "What is the value of i⁴?", "opts": {"a": "1", "b": "-1", "c": "i", "d": "-i"}, "ans": "a"},
        {"q": "What is the modulus of the complex number z = -5 + 12i?", "opts": {"a": "13", "b": "17", "c": "7", "d": "12"}, "ans": "a"},
        {"q": "If z = a + bi, which of the following represents the modulus |z|?", "opts": {"a": "√(a² + b²)", "b": "a² + b²", "c": "a + b", "d": "√(a² - b²)"}, "ans": "a"},
        {"q": "Solve for the conjugate of z = -4 - i.", "opts": {"a": "-4 + i", "b": "4 - i", "c": "4 + i", "d": "-4 - i"}, "ans": "a"},
        {"q": "Add the complex numbers: -2i + (3 + 4i).", "opts": {"a": "3 + 2i", "b": "1 + 4i", "c": "3 - 2i", "d": "5i"}, "ans": "a"},
        {"q": "What is the value of i⁵?", "opts": {"a": "i", "b": "-i", "c": "1", "d": "-1"}, "ans": "a"},
        {"q": "What is the real part of the complex number z = -7i?", "opts": {"a": "0", "b": "-7", "c": "-7i", "d": "7"}, "ans": "a"},
        {"q": "What is the imaginary part of the complex number z = 12?", "opts": {"a": "0", "b": "12", "c": "i", "d": "12i"}, "ans": "a"},
        {"q": "What is the modulus of the complex number z = -6i?", "opts": {"a": "6", "b": "-6", "c": "36", "d": "0"}, "ans": "a"},
        {"q": "What is the conjugate of the complex number z = -8?", "opts": {"a": "-8", "b": "8", "c": "-8i", "d": "8i"}, "ans": "a"},
        {"q": "Simplify: 3(2 + 4i).", "opts": {"a": "6 + 12i", "b": "6 + 4i", "c": "5 + 7i", "d": "6 - 12i"}, "ans": "a"},
        {"q": "Simplify: -2(3 - 5i).", "opts": {"a": "-6 + 10i", "b": "-6 - 10i", "c": "6 - 10i", "d": "-6 + 5i"}, "ans": "a"},
        {"q": "What is the modulus of the complex number z = 1 + i?", "opts": {"a": "√2", "b": "2", "c": "1", "d": "0"}, "ans": "a"},
        {"q": "Express the complex number z = i in terms of real and imaginary parts.", "opts": {"a": "0 + 1i", "b": "1 + 0i", "c": "0 - 1i", "d": "1 + 1i"}, "ans": "a"},
        {"q": "Simplify: i + i² + i³.", "opts": {"a": "-1", "b": "0", "c": "i", "d": "-i"}, "ans": "a"},
        {"q": "What is the value of i^10?", "opts": {"a": "-1", "b": "1", "c": "i", "d": "-i"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "Multiply the complex numbers: (2 + 3i)(1 + 2i).", "opts": {"a": "-4 + 7i", "b": "8 + 7i", "c": "2 + 6i", "d": "-4 + 6i"}, "ans": "a"},
        {"q": "Multiply the complex numbers: (3 - i)(2 + 4i).", "opts": {"a": "10 + 10i", "b": "6 - 4i", "c": "10 - 10i", "d": "6 + 10i"}, "ans": "a"},
        {"q": "Simplify the expression: (2 + i) / i.", "opts": {"a": "1 - 2i", "b": "2 - i", "c": "-1 + 2i", "d": "2i - 1"}, "ans": "a"},
        {"q": "Evaluate: (1 + i)².", "opts": {"a": "2i", "b": "2", "c": "1 + 2i", "d": "-2i"}, "ans": "a"},
        {"q": "Evaluate: (1 - i)².", "opts": {"a": "-2i", "b": "-2", "c": "1 - 2i", "d": "2i"}, "ans": "a"},
        {"q": "Divide: (3 + 4i) / (1 - 2i).", "opts": {"a": "-1 + 2i", "b": "11/5 + 2/5i", "c": "-1 + 10i", "d": "-1 - 2i"}, "ans": "a"},
        {"q": "Divide: (5 - 5i) / (2 - i).", "opts": {"a": "3 - i", "b": "3 + i", "c": "1 - 3i", "d": "2 - 3i"}, "ans": "a"},
        {"q": "Find the modulus of the product: (1 + 2i)(3 - 4i).", "opts": {"a": "5√5", "b": "25", "c": "5", "d": "2√5"}, "ans": "a"},
        {"q": "If z = 2 + i, find z * conjugate(z).", "opts": {"a": "5", "b": "3", "c": "4 - i", "d": "√5"}, "ans": "a"},
        {"q": "What is the argument (in radians) of the complex number z = 1 + i?", "opts": {"a": "π/4", "b": "π/2", "c": "π/3", "d": "π/6"}, "ans": "a"},
        {"q": "What is the argument (in radians) of the complex number z = 1 - i?", "opts": {"a": "-π/4 (or 7π/4)", "b": "π/4", "c": "3π/4", "d": "5π/4"}, "ans": "a"},
        {"q": "Find the argument of the complex number z = -√3 + i.", "opts": {"a": "5π/6", "b": "π/6", "c": "2π/3", "d": "5π/3"}, "ans": "a"},
        {"q": "Solve for the real values of x and y in the equation: x + 2i + y - yi = 5 + 3i.", "opts": {"a": "x = 6, y = -1", "b": "x = 2, y = 3", "c": "x = 5, y = -1", "d": "x = 8, y = -3"}, "ans": "a"},
        {"q": "Solve for x and y: (x + yi)(2 - i) = 5.", "opts": {"a": "x = 2, y = 1", "b": "x = 2, y = -1", "c": "x = 1, y = 2", "d": "x = 1, y = -2"}, "ans": "a"},
        {"q": "Find the polar form of the complex number z = 1 + √3i.", "opts": {"a": "2(cos(π/3) + i sin(π/3))", "b": "2(cos(π/6) + i sin(π/6))", "c": "4(cos(π/3) + i sin(π/3))", "d": "2(cos(2π/3) + i sin(2π/3))"}, "ans": "a"},
        {"q": "Find the polar form of the complex number z = -1 + i.", "opts": {"a": "√2(cos(3π/4) + i sin(3π/4))", "b": "√2(cos(π/4) + i sin(π/4))", "c": "2(cos(3π/4) + i sin(3π/4))", "d": "√2(cos(5π/4) + i sin(5π/4))"}, "ans": "a"},
        {"q": "Simplify the expression: (2 - 3i)(2 + 3i).", "opts": {"a": "13", "b": "-5", "c": "4 - 9i", "d": "5"}, "ans": "a"},
        {"q": "If z1 = 3 + 2i and z2 = 1 - i, find z1 * z2.", "opts": {"a": "5 - i", "b": "1 + i", "c": "3 - 2i", "d": "5 + i"}, "ans": "a"},
        {"q": "Simplify: i^100.", "opts": {"a": "1", "b": "-1", "c": "i", "d": "-i"}, "ans": "a"},
        {"q": "Simplify: i^2009.", "opts": {"a": "i", "b": "-i", "c": "1", "d": "-1"}, "ans": "a"},
        {"q": "What is the modulus of the reciprocal of z = 3 - 4i?", "opts": {"a": "1/5", "b": "5", "c": "1/25", "d": "25"}, "ans": "a"},
        {"q": "If z = cos(θ) + i sin(θ), what is the modulus of z?", "opts": {"a": "1", "b": "cos(θ)", "c": "sin(θ)", "d": "0"}, "ans": "a"},
        {"q": "Find the complex number representing the point (-3, 3) on the Argand diagram.", "opts": {"a": "-3 + 3i", "b": "3 - 3i", "c": "-3 - 3i", "d": "3 + 3i"}, "ans": "a"},
        {"q": "Simplify: (2i)³.", "opts": {"a": "-8i", "b": "8i", "c": "-8", "d": "8"}, "ans": "a"},
        {"q": "Evaluate: (1 + i)^4.", "opts": {"a": "-4", "b": "4i", "c": "-4i", "d": "4"}, "ans": "a"},
        {"q": "Find the square of the complex number z = 2i.", "opts": {"a": "-4", "b": "4i", "c": "4", "d": "-4i"}, "ans": "a"},
        {"q": "Simplify the complex expression: (i - 1)(i + 1).", "opts": {"a": "-2", "b": "0", "c": "-2i", "d": "2"}, "ans": "a"},
        {"q": "If z = 2 + 5i, what is z + conjugate(z)?", "opts": {"a": "4", "b": "10i", "c": "4 + 10i", "d": "29"}, "ans": "a"},
        {"q": "If z = 2 + 5i, what is z - conjugate(z)?", "opts": {"a": "10i", "b": "4", "c": "4 + 10i", "d": "29"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Simplify the expression using De Moivre's Theorem: (1 + i)^8.", "opts": {"a": "16", "b": "16i", "c": "-16", "d": "32"}, "ans": "a"},
        {"q": "Simplify the expression using De Moivre's Theorem: (1 - √3i)^6.", "opts": {"a": "64", "b": "-64", "c": "64i", "d": "-64i"}, "ans": "a"},
        {"q": "Find the three cube roots of 1 in complex numbers.", "opts": {"a": "1, -1/2 + √3/2i, and -1/2 - √3/2i", "b": "1, i, and -i", "c": "1, 1/2 + √3/2i, and 1/2 - √3/2i", "d": "1, -1, and i"}, "ans": "a"},
        {"q": "Solve the quadratic equation in the complex system: z² - 2z + 5 = 0.", "opts": {"a": "1 ± 2i", "b": "2 ± 4i", "c": "-1 ± 2i", "d": "1 ± i"}, "ans": "a"},
        {"q": "Solve the quadratic equation in the complex system: z² + 4z + 13 = 0.", "opts": {"a": "-2 ± 3i", "b": "-2 ± 9i", "c": "2 ± 3i", "d": "-4 ± 3i"}, "ans": "a"},
        {"q": "Evaluate the complex number expression: (1 + i)^10 / (1 - i)^8.", "opts": {"a": "2i", "b": "-2i", "c": "2", "d": "16i"}, "ans": "a"},
        {"q": "Find the modulus and argument of the complex number z = (2 + 2i) / (1 - √3i).", "opts": {"a": "Modulus √2, Argument -5π/12", "b": "Modulus 2, Argument π/12", "c": "Modulus √2, Argument 7π/12", "d": "Modulus 1, Argument -π/4"}, "ans": "a"},
        {"q": "If z = cos(θ) + i sin(θ), express 1/z according to De Moivre's Theorem.", "opts": {"a": "cos(θ) - i sin(θ)", "b": "cos(-θ) - i sin(-θ)", "c": "-cos(θ) + i sin(θ)", "d": "1 / (cos(θ) - i sin(θ))"}, "ans": "a"},
        {"q": "Find the square roots of the complex number z = 3 + 4i.", "opts": {"a": "±(2 + i)", "b": "±(1 + 2i)", "c": "±(2 - i)", "d": "±(3 + i)"}, "ans": "a"},
        {"q": "Find the square roots of the complex number z = -8 - 6i.", "opts": {"a": "±(1 - 3i)", "b": "±(3 - i)", "c": "±(1 + 3i)", "d": "±(3 + i)"}, "ans": "a"},
        {"q": "If |z - 3| = |z + 3i|, describe the locus of the point z on the Argand diagram.", "opts": {"a": "The line y = -x", "b": "The circle x² + y² = 9", "c": "The line y = x", "d": "The line x = y"}, "ans": "a"},
        {"q": "If |z - i| = 2, describe the locus of the point z on the Argand diagram.", "opts": {"a": "A circle with center (0, 1) and radius 2", "b": "A line parallel to the x-axis", "c": "A circle with center (1, 0) and radius 2", "d": "A line parallel to the y-axis"}, "ans": "a"},
        {"q": "Simplify: cos(3θ) + i sin(3θ) * (cos(2θ) - i sin(2θ)).", "opts": {"a": "cos(θ) + i sin(θ)", "b": "cos(5θ) + i sin(5θ)", "c": "cos(θ) - i sin(θ)", "d": "cos(5θ) - i sin(5θ)"}, "ans": "a"},
        {"q": "Solve the complex equation: z + 2 * conjugate(z) = 6 - 3i.", "opts": {"a": "z = 2 + 3i", "b": "z = 2 - 3i", "c": "z = -2 + 3i", "d": "z = 3 + 2i"}, "ans": "a"},
        {"q": "Evaluate: (√3/2 + 1/2i)^12.", "opts": {"a": "1", "b": "-1", "c": "i", "d": "-i"}, "ans": "a"},
        {"q": "Express the complex number z = 3(cos(5π/6) - i sin(5π/6)) in standard polar form.", "opts": {"a": "3(cos(-5π/6) + i sin(-5π/6))", "b": "3(cos(5π/6) + i sin(5π/6))", "c": "3(cos(π/6) + i sin(π/6))", "d": "3(cos(-π/6) + i sin(-π/6))"}, "ans": "a"},
        {"q": "Determine the modulus of: (2 + i)³ / (1 - i)^4.", "opts": {"a": "5√5 / 4", "b": "5√5", "c": "5/4", "d": "25 / 4"}, "ans": "a"},
        {"q": "If z = x + yi and Re(z²) = 0, describe the locus of z.", "opts": {"a": "The lines y = ±x", "b": "The coordinate axes (x = 0 or y = 0)", "c": "The circle x² + y² = 1", "d": "The line y = 0"}, "ans": "a"},
        {"q": "If z = x + yi and Im(z²) = 0, describe the locus of z.", "opts": {"a": "The coordinate axes (x = 0 or y = 0)", "b": "The lines y = ±x", "c": "The circle x² + y² = 1", "d": "The line x = 0"}, "ans": "a"},
        {"q": "Find the polar coordinates of the complex number z = -3i.", "opts": {"a": "(3, 3π/2)", "b": "(3, π/2)", "c": "(3, -π/2)", "d": "(3, π)"}, "ans": "a"},
        {"q": "Express the complex number z = 4e^(iπ/3) in polar trigonometric form.", "opts": {"a": "4(cos(π/3) + i sin(π/3))", "b": "4(cos(π/6) + i sin(π/6))", "c": "2(cos(π/3) + i sin(π/3))", "d": "4(cos(2π/3) + i sin(2π/3))"}, "ans": "a"},
        {"q": "Determine the value of |e^(ix)| for any real number x.", "opts": {"a": "1", "b": "e^x", "c": "cos(x)", "d": "sin(x)"}, "ans": "a"},
        {"q": "If z = 2(cos(π/4) + i sin(π/4)), find z³.", "opts": {"a": "8(cos(3π/4) + i sin(3π/4))", "b": "8(cos(π/4) + i sin(π/4))", "c": "6(cos(3π/4) + i sin(3π/4))", "d": "8(cos(5π/4) + i sin(5π/4))"}, "ans": "a"},
        {"q": "Solve for the complex root: z³ = -8i.", "opts": {"a": "2i, √3 - i, and -√3 - i", "b": "2i, √3 + i, and -√3 + i", "c": "-2i, √3 - i, and -√3 - i", "d": "-2i, √3 + i, and -√3 + i"}, "ans": "a"},
        {"q": "If w is a non-real cube root of unity, simplify: 1 + w + w².", "opts": {"a": "0", "b": "1", "c": "w", "d": "-1"}, "ans": "a"},
        {"q": "If w is a non-real cube root of unity, evaluate: (1 - w + w²)(1 + w - w²).", "opts": {"a": "4", "b": "2", "c": "0", "d": "1"}, "ans": "a"},
        {"q": "Find the product: e^(iπ/4) * e^(iπ/2).", "opts": {"a": "e^(i3π/4)", "b": "e^(iπ/8)", "c": "e^(i3π/2)", "d": "e^(i5π/4)"}, "ans": "a"},
        {"q": "What is the argument of the complex number z = -2 - 2i?", "opts": {"a": "5π/4 (or -3π/4)", "b": "3π/4", "c": "π/4", "d": "7π/4"}, "ans": "a"},
        {"q": "Solve for z in: (z - 1) / (z + 1) = i.", "opts": {"a": "i", "b": "-i", "c": "1 + i", "d": "1 - i"}, "ans": "a"},
        {"q": "Calculate the value of |(3 + i)^4|.", "opts": {"a": "100", "b": "10", "c": "20", "d": "10000"}, "ans": "a"},
        {"q": "Express standard complex division in terms of modulus and argument: |z1/z2| and arg(z1/z2).", "opts": {"a": "|z1|/|z2| and arg(z1) - arg(z2)", "b": "|z1|*|z2| and arg(z1) + arg(z2)", "c": "|z1|/|z2| and arg(z1) + arg(z2)", "d": "|z1|*|z2| and arg(z1) - arg(z2)"}, "ans": "a"},
        {"q": "If z = cos(θ) + i sin(θ), find the real part of (z - 1) / (z + 1).", "opts": {"a": "0", "b": "cos(θ)", "c": "sin(θ)", "d": "tan(θ/2)"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch6_questions():
    # Chapter 6: Differentiation
    # Focus: Derivatives using power rule, product rule, quotient rule, chain rule, tangent/normal slopes, stationary points.
    easy = [
        {"q": "Find the derivative of the function f(x) = x³.", "opts": {"a": "3x²", "b": "x²", "c": "3x", "d": "3x³"}, "ans": "a"},
        {"q": "Find the derivative of the function f(x) = 5x.", "opts": {"a": "5", "b": "5x", "c": "1", "d": "0"}, "ans": "a"},
        {"q": "Find the derivative of the function f(x) = 7.", "opts": {"a": "0", "b": "7", "c": "1", "d": "7x"}, "ans": "a"},
        {"q": "What is the derivative of the function f(x) = x² + 4x?", "opts": {"a": "2x + 4", "b": "2x", "c": "x + 4", "d": "2x² + 4"}, "ans": "a"},
        {"q": "Find the derivative of the function f(x) = 3x² - 5x + 2.", "opts": {"a": "6x - 5", "b": "6x - 5 + 2", "c": "3x - 5", "d": "6x"}, "ans": "a"},
        {"q": "What is the derivative of f(x) = sin(x)?", "opts": {"a": "cos(x)", "b": "-cos(x)", "c": "sin(x)", "d": "-sin(x)"}, "ans": "a"},
        {"q": "What is the derivative of f(x) = cos(x)?", "opts": {"a": "-sin(x)", "b": "sin(x)", "c": "cos(x)", "d": "-cos(x)"}, "ans": "a"},
        {"q": "What is the derivative of f(x) = e^x?", "opts": {"a": "e^x", "b": "xe^(x-1)", "c": "1", "d": "ln(x)"}, "ans": "a"},
        {"q": "Find the slope of the tangent line to the curve y = x² at x = 3.", "opts": {"a": "6", "b": "9", "c": "3", "d": "2"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = 2x^4.", "opts": {"a": "8x³", "b": "4x³", "c": "8x", "d": "2x³"}, "ans": "a"},
        {"q": "What is the slope of a line tangent to y = x³ - 3x at x = 1?", "opts": {"a": "0", "b": "1", "c": "-3", "d": "3"}, "ans": "a"},
        {"q": "What is the power rule for differentiation?", "opts": {"a": "d/dx(x^n) = n * x^(n-1)", "b": "d/dx(x^n) = x^(n+1) / (n+1)", "c": "d/dx(x^n) = n * x^n", "d": "d/dx(x^n) = x^(n-1)"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = x^10.", "opts": {"a": "10x^9", "b": "9x^10", "c": "10x^10", "d": "9x^9"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = 1/x.", "opts": {"a": "-1/x²", "b": "1/x²", "c": "ln(x)", "d": "-1/x"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = √x.", "opts": {"a": "1 / (2√x)", "b": "2√x", "c": "1 / √x", "d": "1/2 * x^(1/2)"}, "ans": "a"},
        {"q": "Find the slope of the tangent to the curve y = 4x at x = 2.", "opts": {"a": "4", "b": "8", "c": "2", "d": "0"}, "ans": "a"},
        {"q": "If y = x² - 2x + 1, find dy/dx.", "opts": {"a": "2x - 2", "b": "2x - 1", "c": "2x", "d": "x - 2"}, "ans": "a"},
        {"q": "Find the derivative of y = -3x³.", "opts": {"a": "-9x²", "b": "-9x", "c": "-3x²", "d": "9x²"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = 4 - x².", "opts": {"a": "-2x", "b": "2x", "c": "4 - 2x", "d": "0"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = 2x³ + 5x².", "opts": {"a": "6x² + 10x", "b": "6x² + 5x", "c": "3x² + 10x", "d": "6x + 10"}, "ans": "a"},
        {"q": "What is the derivative of the constant function f(x) = c?", "opts": {"a": "0", "b": "c", "c": "1", "d": "cx"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = 3x + 10.", "opts": {"a": "3", "b": "3x", "c": "10", "d": "0"}, "ans": "a"},
        {"q": "Find the slope of the curve y = x³ at the point (1, 1).", "opts": {"a": "3", "b": "1", "c": "2", "d": "0"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = ln(x).", "opts": {"a": "1/x", "b": "e^x", "c": "1/x²", "d": "1"}, "ans": "a"},
        {"q": "What is the value of dy/dx for y = 2x² at x = -1?", "opts": {"a": "-4", "b": "4", "c": "-2", "d": "2"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "Find the derivative of f(x) = sin(2x) using the chain rule.", "opts": {"a": "2 cos(2x)", "b": "cos(2x)", "c": "-2 cos(2x)", "d": "2 sin(2x)"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = cos(3x) using the chain rule.", "opts": {"a": "-3 sin(3x)", "b": "3 sin(3x)", "c": "-sin(3x)", "d": "-3 cos(3x)"}, "ans": "a"},
        {"q": "Use the product rule to find the derivative of f(x) = x * sin(x).", "opts": {"a": "sin(x) + x cos(x)", "b": "x cos(x)", "c": "sin(x) - x cos(x)", "d": "cos(x)"}, "ans": "a"},
        {"q": "Use the product rule to find the derivative of f(x) = x² * e^x.", "opts": {"a": "x²e^x + 2xe^x", "b": "2xe^x", "c": "x²e^x", "d": "x²e^x + xe^x"}, "ans": "a"},
        {"q": "Use the quotient rule to find the derivative of f(x) = sin(x) / x.", "opts": {"a": "(x cos(x) - sin(x)) / x²", "b": "(sin(x) - x cos(x)) / x²", "c": "(x cos(x) + sin(x)) / x²", "d": "cos(x) / 1"}, "ans": "a"},
        {"q": "Use the quotient rule to find the derivative of f(x) = x / (x + 1).", "opts": {"a": "1 / (x + 1)²", "b": "1 / (x + 1)", "c": "(2x + 1) / (x + 1)²", "d": "-1 / (x + 1)²"}, "ans": "a"},
        {"q": "Find the equation of the tangent line to y = x² - 3x at the point (1, -2).", "opts": {"a": "y = -x - 1", "b": "y = -x - 2", "c": "y = -3x + 1", "d": "y = 2x - 4"}, "ans": "a"},
        {"q": "Find the coordinates of the stationary point(s) of the function f(x) = x² - 4x + 5.", "opts": {"a": "(2, 1)", "b": "(2, 5)", "c": "(4, 5)", "d": "(1, 2)"}, "ans": "a"},
        {"q": "Find the second derivative of the function f(x) = x³ - 5x² + 2x.", "opts": {"a": "6x - 10", "b": "3x² - 10x + 2", "c": "6", "d": "6x"}, "ans": "a"},
        {"q": "Determine the nature of the stationary point of f(x) = x² - 4x + 5.", "opts": {"a": "Minimum point (second derivative > 0)", "b": "Maximum point (second derivative < 0)", "c": "Point of inflection", "d": "None of the above"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = (2x + 3)^5 using the chain rule.", "opts": {"a": "10(2x + 3)^4", "b": "5(2x + 3)^4", "c": "10(2x + 3)^5", "d": "20(2x + 3)^4"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = ln(3x + 1) using the chain rule.", "opts": {"a": "3 / (3x + 1)", "b": "1 / (3x + 1)", "c": "3ln(3x + 1)", "d": "1 / 3x"}, "ans": "a"},
        {"q": "What is the slope of the normal line to y = x² at the point (2, 4)?", "opts": {"a": "-1/4", "b": "4", "c": "-4", "d": "1/4"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = tan(x).", "opts": {"a": "sec²(x)", "b": "-sec²(x)", "c": "csc²(x)", "d": "sec(x)tan(x)"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = sec(x).", "opts": {"a": "sec(x)tan(x)", "b": "sec²(x)", "c": "tan²(x)", "d": "csc(x)cot(x)"}, "ans": "a"},
        {"q": "Determine the derivative of f(x) = e^(2x).", "opts": {"a": "2e^(2x)", "b": "e^(2x)", "c": "2xe^(2x-1)", "d": "1/2 * e^(2x)"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = ln(x²).", "opts": {"a": "2/x", "b": "1/x²", "c": "2x/x²", "d": "2ln(x)"}, "ans": "a"},
        {"q": "The displacement of a particle is given by s(t) = t² - 4t + 3. Find its velocity at t = 3.", "opts": {"a": "2", "b": "-1", "c": "0", "d": "3"}, "ans": "a"},
        {"q": "The displacement of a particle is given by s(t) = t² - 4t + 3. At what time is the particle at rest?", "opts": {"a": "t = 2", "b": "t = 4", "c": "t = 0", "d": "t = 3"}, "ans": "a"},
        {"q": "Find the stationary points of f(x) = x³ - 3x.", "opts": {"a": "(1, -2) and (-1, 2)", "b": "(0, 0)", "c": "(1, -2)", "d": "(2, 2) and (-2, -2)"}, "ans": "a"},
        {"q": "Determine the nature of the stationary point of f(x) = -x² + 6x.", "opts": {"a": "Maximum point", "b": "Minimum point", "c": "Inflection point", "d": "None"}, "ans": "a"},
        {"q": "Find the derivative of y = (x² + 1)³.", "opts": {"a": "6x(x² + 1)²", "b": "3(x² + 1)²", "c": "6x(x² + 1)³", "d": "2x(x² + 1)²"}, "ans": "a"},
        {"q": "Simplify the derivative of y = ln(sin(x)).", "opts": {"a": "cot(x)", "b": "tan(x)", "c": "1/sin(x)", "d": "cos(x)/x"}, "ans": "a"},
        {"q": "Simplify the derivative of y = ln(cos(x)).", "opts": {"a": "-tan(x)", "b": "tan(x)", "c": "cot(x)", "d": "-cot(x)"}, "ans": "a"},
        {"q": "Find the slope of the tangent to the curve y = cos(2x) at x = π/4.", "opts": {"a": "-2", "b": "0", "c": "2", "d": "-1"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = x * ln(x).", "opts": {"a": "ln(x) + 1", "b": "ln(x)", "c": "1", "d": "1/x"}, "ans": "a"},
        {"q": "Find the coordinates of the point on y = x² - 4x where the tangent is horizontal.", "opts": {"a": "(2, -4)", "b": "(2, 0)", "c": "(0, 0)", "d": "(4, 0)"}, "ans": "a"},
        {"q": "Find the acceleration of a particle at t = 2 if its velocity is v(t) = 3t² - 2t.", "opts": {"a": "10", "b": "8", "c": "12", "d": "6"}, "ans": "a"},
        {"q": "If f(x) = x + 1/x, find f'(x).", "opts": {"a": "1 - 1/x²", "b": "1 + 1/x²", "c": "1 - x²", "d": "ln(x)"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Find the derivative of the function f(x) = sin³(4x² + 1) using the chain rule.", "opts": {"a": "24x * sin²(4x² + 1) * cos(4x² + 1)", "b": "3 sin²(4x² + 1) * cos(4x² + 1)", "c": "24x * sin²(4x² + 1)", "d": "8x * cos³(4x² + 1)"}, "ans": "a"},
        {"q": "Find the derivative dy/dx of the implicitly defined curve: x² + y² = 25.", "opts": {"a": "-x / y", "b": "-y / x", "c": "x / y", "d": "-2x / 2y"}, "ans": "a"},
        {"q": "Find the derivative dy/dx of the implicitly defined curve: x³ + y³ = 3xy.", "opts": {"a": "(y - x²) / (y² - x)", "b": "(x² - y) / (y² - x)", "c": "(y - x²) / (x - y²)", "d": "(3x - 3y²) / 3x"}, "ans": "a"},
        {"q": "Find the equation of the tangent line to the implicitly defined curve x² + xy + y² = 7 at the point (1, 2).", "opts": {"a": "4x + 5y - 14 = 0", "b": "4x - 5y + 6 = 0", "c": "5x + 4y - 13 = 0", "d": "4x + 5y - 12 = 0"}, "ans": "a"},
        {"q": "Find the stationary points of the function f(x) = 2x³ - 3x² - 12x + 5, and determine their nature.", "opts": {"a": "Local Max at (-1, 12), Local Min at (2, -15)", "b": "Local Min at (-1, 12), Local Max at (2, -15)", "c": "Local Max at (-1, 5), Local Min at (2, 5)", "d": "Stationary points at x = 1, 2"}, "ans": "a"},
        {"q": "A closed cylindrical can is to be made to contain 16π cm³ of liquid. Find the dimensions (radius r and height h) that minimize the surface area.", "opts": {"a": "r = 2 cm, h = 4 cm", "b": "r = 4 cm, h = 2 cm", "c": "r = 1 cm, h = 16 cm", "d": "r = 2 cm, h = 2 cm"}, "ans": "a"},
        {"q": "A rectangle is inscribed under the curve y = 9 - x² in the first quadrant, with one vertex on the curve and one at the origin. Find the maximum area of the rectangle.", "opts": {"a": "6√3", "b": "18", "c": "9", "d": "12√3"}, "ans": "a"},
        {"q": "Find the derivative of the function f(x) = x^x using logarithmic differentiation.", "opts": {"a": "x^x * (ln(x) + 1)", "b": "x * x^(x-1)", "c": "x^x * ln(x)", "d": "x^x"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = arctan(x).", "opts": {"a": "1 / (1 + x²)", "b": "-1 / (1 + x²)", "c": "1 / √(1 - x²)", "d": "sec²(x)"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = arcsin(x).", "opts": {"a": "1 / √(1 - x²)", "b": "-1 / √(1 - x²)", "c": "1 / (1 + x²)", "d": "cos(x)"}, "ans": "a"},
        {"q": "What is the derivative of f(x) = arccos(x)?", "opts": {"a": "-1 / √(1 - x²)", "b": "1 / √(1 - x²)", "c": "-1 / (1 + x²)", "d": "-sin(x)"}, "ans": "a"},
        {"q": "Find the derivative of y = ln((x - 1)/(x + 1)) using log properties.", "opts": {"a": "2 / (x² - 1)", "b": "1 / (x - 1) + 1 / (x + 1)", "c": "2 / (x² + 1)", "d": "1 / (x² - 1)"}, "ans": "a"},
        {"q": "Find the equation of the normal line to the curve y = ln(x) at the point where it crosses the x-axis.", "opts": {"a": "x + y - 1 = 0", "b": "x - y - 1 = 0", "c": "x + y + 1 = 0", "d": "y = -x"}, "ans": "a"},
        {"q": "Find the second derivative of y = tan(x).", "opts": {"a": "2 sec²(x) tan(x)", "b": "sec²(x) tan(x)", "c": "2 sec(x) tan(x)", "d": "2 sec²(x)"}, "ans": "a"},
        {"q": "What is the value of the derivative of f(x) = x³ * ln(x) at x = e?", "opts": {"a": "4e²", "b": "3e² + e²", "c": "e³", "d": "4e³"}, "ans": "a"},
        {"q": "If y = cos²(x²), find dy/dx.", "opts": {"a": "-4x * cos(x²) * sin(x²)", "b": "-2 * cos(x²) * sin(x²)", "c": "-4x * cos(x²)", "d": "-2x * sin(2x²)"}, "ans": "a"},
        {"q": "Find the coordinates of the point of inflection of the curve y = x³ - 3x² + 4.", "opts": {"a": "(1, 2)", "b": "(1, 0)", "c": "(0, 4)", "d": "(2, 0)"}, "ans": "a"},
        {"q": "A spherical balloon is being inflated at a rate of 10 cm³/s. Find the rate of increase of the radius when r = 5 cm.", "opts": {"a": "1 / (10π) cm/s", "b": "1 / (5π) cm/s", "c": "1 / (25π) cm/s", "d": "10π cm/s"}, "ans": "a"},
        {"q": "If x = t² + t and y = t³ - t, find the parametric derivative dy/dx.", "opts": {"a": "(3t² - 1) / (2t + 1)", "b": "(2t + 1) / (3t² - 1)", "c": "3t² - 1", "d": "2t + 1"}, "ans": "a"},
        {"q": "For the curve x = cos(t), y = sin(t), find d²y/dx² at t = π/4.", "opts": {"a": "-2√2", "b": "-√2", "c": "√2", "d": "2√2"}, "ans": "a"},
        {"q": "Find the derivative of y = 2^x.", "opts": {"a": "2^x * ln(2)", "b": "x * 2^(x-1)", "c": "2^x / ln(2)", "d": "2^x"}, "ans": "a"},
        {"q": "Find the derivative of y = log10(x).", "opts": {"a": "1 / (x * ln(10))", "b": "1 / x", "c": "ln(10) / x", "d": "1 / (10x)"}, "ans": "a"},
        {"q": "If y = sqrt(x + sqrt(x)), find dy/dx.", "opts": {"a": "(2sqrt(x) + 1) / (4sqrt(x) * sqrt(x + sqrt(x)))", "b": "1 / (2sqrt(x + sqrt(x)))", "c": "(2sqrt(x) + 1) / (2sqrt(x + sqrt(x)))", "d": "1"}, "ans": "a"},
        {"q": "Determine the limit: lim x->0 (sin(x)/x).", "opts": {"a": "1", "b": "0", "c": "undefined", "d": "infinite"}, "ans": "a"},
        {"q": "Find the maximum product of two numbers whose sum is 20.", "opts": {"a": "100", "b": "99", "c": "120", "d": "75"}, "ans": "a"},
        {"q": "Find the derivative of y = x^(1/x) using logarithmic differentiation.", "opts": {"a": "x^(1/x) * (1 - ln(x)) / x²", "b": "x^(1/x) * ln(x) / x²", "c": "1/x * x^(1/x - 1)", "d": "x^(1/x) * (ln(x) - 1) / x²"}, "ans": "a"},
        {"q": "Find the value of c in the Mean Value Theorem for f(x) = x² on [0, 2].", "opts": {"a": "1", "b": "1/2", "c": "1.5", "d": "√2"}, "ans": "a"},
        {"q": "Determine the derivative of y = cos(x) * e^(sin(x)).", "opts": {"a": "e^(sin(x)) * (cos²(x) - sin(x))", "b": "e^(sin(x)) * cos²(x)", "c": "-sin(x) * e^(sin(x))", "d": "e^(sin(x)) * (sin(x) - cos²(x))"}, "ans": "a"},
        {"q": "Determine the derivative of y = csc(x).", "opts": {"a": "-csc(x)cot(x)", "b": "csc(x)cot(x)", "c": "-csc²(x)", "d": "-sec(x)tan(x)"}, "ans": "a"},
        {"q": "Determine the derivative of y = cot(x).", "opts": {"a": "-csc²(x)", "b": "csc²(x)", "c": "-sec²(x)", "d": "-cot²(x)"}, "ans": "a"},
        {"q": "Find the derivative of f(x) = ln(x + √(x² + 1)).", "opts": {"a": "1 / √(x² + 1)", "b": "1 / (x + √(x² + 1))", "c": "1", "d": "x / √(x² + 1)"}, "ans": "a"},
        {"q": "If y = x/(x² + 1), find the x-values of the stationary points.", "opts": {"a": "±1", "b": "0", "c": "±2", "d": "no stationary points"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch7_questions():
    # Chapter 7: Limits, Continuity and Integration
    # Focus: Evaluating algebraic limits, continuity, indefinite integrals, definite integrals, area under curves.
    easy = [
        {"q": "Evaluate the limit: lim x->3 (2x + 5).", "opts": {"a": "11", "b": "5", "c": "8", "d": "13"}, "ans": "a"},
        {"q": "Evaluate the limit: lim x->2 (x² - 1).", "opts": {"a": "3", "b": "4", "c": "2", "d": "5"}, "ans": "a"},
        {"q": "What is the indefinite integral of f(x) = 2x dx?", "opts": {"a": "x² + C", "b": "2x² + C", "c": "x²", "d": "2 + C"}, "ans": "a"},
        {"q": "Find the indefinite integral of f(x) = 3x² dx.", "opts": {"a": "x³ + C", "b": "3x³ + C", "c": "x³", "d": "6x + C"}, "ans": "a"},
        {"q": "What is the indefinite integral of a constant k dx?", "opts": {"a": "kx + C", "b": "k + C", "c": "1/2 kx² + C", "d": "C"}, "ans": "a"},
        {"q": "Evaluate the definite integral from 1 to 3 of 2 dx.", "opts": {"a": "4", "b": "2", "c": "6", "d": "8"}, "ans": "a"},
        {"q": "Evaluate the definite integral from 0 to 2 of x dx.", "opts": {"a": "2", "b": "4", "c": "1", "d": "0"}, "ans": "a"},
        {"q": "Find the limit: lim x->0 (x² + 4x - 1).", "opts": {"a": "-1", "b": "0", "c": "4", "d": "undefined"}, "ans": "a"},
        {"q": "What is the integral of cos(x) dx?", "opts": {"a": "sin(x) + C", "b": "-sin(x) + C", "c": "cos(x) + C", "d": "-cos(x) + C"}, "ans": "a"},
        {"q": "What is the integral of sin(x) dx?", "opts": {"a": "-cos(x) + C", "b": "cos(x) + C", "c": "-sin(x) + C", "d": "sin(x) + C"}, "ans": "a"},
        {"q": "Find the indefinite integral of e^x dx.", "opts": {"a": "e^x + C", "b": "xe^(x-1) + C", "c": "ln(x) + C", "d": "e^x"}, "ans": "a"},
        {"q": "What is the indefinite integral of 1/x dx (for x > 0)?", "opts": {"a": "ln(x) + C", "b": "-1/x² + C", "c": "ln|x|", "d": "x + C"}, "ans": "a"},
        {"q": "Evaluate the limit: lim x->-1 (3x² - x).", "opts": {"a": "4", "b": "2", "c": "3", "d": "0"}, "ans": "a"},
        {"q": "Evaluate the limit: lim x->5 (4).", "opts": {"a": "4", "b": "5", "c": "0", "d": "undefined"}, "ans": "a"},
        {"q": "What is the integral of x^n dx for n != -1?", "opts": {"a": "x^(n+1) / (n+1) + C", "b": "n * x^(n-1) + C", "c": "x^(n-1) / (n-1) + C", "d": "x^n + C"}, "ans": "a"},
        {"q": "What is the integration constant traditionally denoted as?", "opts": {"a": "C", "b": "k", "c": "x", "d": "a"}, "ans": "a"},
        {"q": "Evaluate the definite integral from 1 to 2 of 3x² dx.", "opts": {"a": "7", "b": "8", "c": "9", "d": "6"}, "ans": "a"},
        {"q": "Find the limit: lim x->2 (3x - 1).", "opts": {"a": "5", "b": "6", "c": "7", "d": "4"}, "ans": "a"},
        {"q": "Evaluate: integral of x³ dx.", "opts": {"a": "1/4 x^4 + C", "b": "3x² + C", "c": "x^4 + C", "d": "1/3 x³ + C"}, "ans": "a"},
        {"q": "Find the limit: lim x->4 (√x).", "opts": {"a": "2", "b": "4", "c": "16", "d": "undefined"}, "ans": "a"},
        {"q": "A function f(x) is continuous at x = a if:", "opts": {"a": "lim x->a f(x) = f(a)", "b": "f(a) is defined", "c": "lim x->a f(x) exists", "d": "f'(a) exists"}, "ans": "a"},
        {"q": "What is the integral of 1/x² dx?", "opts": {"a": "-1/x + C", "b": "1/x + C", "c": "-2/x³ + C", "d": "ln(x²)"}, "ans": "a"},
        {"q": "Evaluate the definite integral from 0 to 1 of e^x dx.", "opts": {"a": "e - 1", "b": "e", "c": "1", "d": "e + 1"}, "ans": "a"},
        {"q": "Evaluate the limit: lim x->0 (cos(x)).", "opts": {"a": "1", "b": "0", "c": "undefined", "d": "-1"}, "ans": "a"},
        {"q": "Find the indefinite integral of 5 dx.", "opts": {"a": "5x + C", "b": "5 + C", "c": "C", "d": "5x² + C"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "Evaluate the limit: lim x->3 (x² - 9) / (x - 3).", "opts": {"a": "6", "b": "3", "c": "0", "d": "undefined"}, "ans": "a"},
        {"q": "Evaluate the limit: lim x->-2 (x² - 4) / (x + 2).", "opts": {"a": "-4", "b": "4", "c": "0", "d": "undefined"}, "ans": "a"},
        {"q": "Evaluate the limit: lim x->1 (x² + 2x - 3) / (x - 1).", "opts": {"a": "4", "b": "3", "c": "2", "d": "0"}, "ans": "a"},
        {"q": "Find the limit at infinity: lim x->∞ (3x² + 2) / (x² - 5).", "opts": {"a": "3", "b": "2", "c": "∞", "d": "-2/5"}, "ans": "a"},
        {"q": "Find the limit at infinity: lim x->∞ (2x + 1) / (3x² - 4).", "opts": {"a": "0", "b": "2/3", "c": "∞", "d": "-1/4"}, "ans": "a"},
        {"q": "Evaluate the definite integral from 0 to π of sin(x) dx.", "opts": {"a": "2", "b": "0", "c": "1", "d": "-2"}, "ans": "a"},
        {"q": "Evaluate the definite integral from 0 to π/2 of cos(x) dx.", "opts": {"a": "1", "b": "0", "c": "2", "d": "-1"}, "ans": "a"},
        {"q": "Find the area under the curve y = 2x from x = 1 to x = 4.", "opts": {"a": "15", "b": "16", "c": "8", "d": "12"}, "ans": "a"},
        {"q": "Find the area under the curve y = x² from x = 0 to x = 3.", "opts": {"a": "9", "b": "27", "c": "3", "d": "18"}, "ans": "a"},
        {"q": "What is the indefinite integral of (2x + 3) dx?", "opts": {"a": "x² + 3x + C", "b": "2x² + 3x + C", "c": "x² + C", "d": "2 + C"}, "ans": "a"},
        {"q": "What is the indefinite integral of (4x³ - 6x) dx?", "opts": {"a": "x^4 - 3x² + C", "b": "4x^4 - 6x² + C", "c": "x^4 - 6x² + C", "d": "12x² - 6 + C"}, "ans": "a"},
        {"q": "If dy/dx = 3x² + 4x and y = 5 when x = 1, find the constant of integration C.", "opts": {"a": "2", "b": "3", "c": "5", "d": "0"}, "ans": "a"},
        {"q": "If dy/dx = 2x - 3 and y = 4 when x = 2, find the function y(x).", "opts": {"a": "y = x² - 3x + 6", "b": "y = x² - 3x + 4", "c": "y = x² - 3x", "d": "y = x² - 3"}, "ans": "a"},
        {"q": "Evaluate the definite integral: integral from 1 to e of (1/x) dx.", "opts": {"a": "1", "b": "e", "c": "0", "d": "ln(e-1)"}, "ans": "a"},
        {"q": "Find the limit: lim x->9 (x - 9) / (√x - 3).", "opts": {"a": "6", "b": "3", "c": "9", "d": "0"}, "ans": "a"},
        {"q": "Find the limit: lim x->0 (e^x - 1) / x. Hint: Use L'Hopital's rule.", "opts": {"a": "1", "b": "0", "c": "e", "d": "undefined"}, "ans": "a"},
        {"q": "Find the vertical asymptote of the function f(x) = 3 / (x - 2).", "opts": {"a": "x = 2", "b": "x = 0", "c": "y = 0", "d": "x = -2"}, "ans": "a"},
        {"q": "Find the horizontal asymptote of the function f(x) = (2x + 1) / (x - 3).", "opts": {"a": "y = 2", "b": "y = 0", "c": "x = 3", "d": "no horizontal asymptote"}, "ans": "a"},
        {"q": "Find the indefinite integral of (e^(2x) + 1) dx.", "opts": {"a": "1/2 * e^(2x) + x + C", "b": "2e^(2x) + x + C", "c": "e^(2x) + x + C", "d": "1/2 * e^(2x) + C"}, "ans": "a"},
        {"q": "Evaluate: integral of (x + 1)² dx.", "opts": {"a": "1/3 (x + 1)³ + C", "b": "1/3 x³ + x² + x + C", "c": "1/2 (x + 1)² + C", "d": "both a and b are correct"}, "ans": "d"},
        {"q": "Find the limit: lim x->∞ (5 - 2/x).", "opts": {"a": "5", "b": "3", "c": "∞", "d": "undefined"}, "ans": "a"},
        {"q": "Evaluate: integral from 0 to 2 of (3x² - 2x) dx.", "opts": {"a": "4", "b": "8", "c": "12", "d": "6"}, "ans": "a"},
        {"q": "If the area under y = kx from x = 0 to x = 2 is 6, solve for k.", "opts": {"a": "3", "b": "2", "c": "1.5", "d": "6"}, "ans": "a"},
        {"q": "What is the integral of sec²(x) dx?", "opts": {"a": "tan(x) + C", "b": "sec(x)tan(x) + C", "c": "-cot(x) + C", "d": "sec(x) + C"}, "ans": "a"},
        {"q": "Evaluate: integral of cos(2x) dx.", "opts": {"a": "1/2 * sin(2x) + C", "b": "2 sin(2x) + C", "c": "-1/2 * sin(2x) + C", "d": "sin(2x) + C"}, "ans": "a"},
        {"q": "Evaluate: integral of sin(3x) dx.", "opts": {"a": "-1/3 * cos(3x) + C", "b": "1/3 * cos(3x) + C", "c": "-3 cos(3x) + C", "d": "cos(3x) + C"}, "ans": "a"},
        {"q": "Find the limit: lim x->0 (x / sin(x)).", "opts": {"a": "1", "b": "0", "c": "undefined", "d": "infinite"}, "ans": "a"},
        {"q": "If f(x) is continuous on [1, 3], and f(1) = -2, f(3) = 4, the Intermediate Value Theorem guarantees that:", "opts": {"a": "f(c) = 0 for some c in (1, 3)", "b": "f'(c) = 3 for some c in (1, 3)", "c": "f(c) = 2 for some c in (1, 3)", "d": "both a and c are guaranteed"}, "ans": "d"},
        {"q": "Evaluate the limit: lim x->4 (x² - 16) / (x² - 4x).", "opts": {"a": "2", "b": "4", "c": "1", "d": "undefined"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Evaluate the limit: lim x->0 (√(x + 4) - 2) / x.", "opts": {"a": "1/4", "b": "1/2", "c": "0", "d": "undefined"}, "ans": "a"},
        {"q": "Evaluate the limit: lim x->0 (1 - cos(x)) / x².", "opts": {"a": "1/2", "b": "1", "c": "0", "d": "undefined"}, "ans": "a"},
        {"q": "Evaluate the limit: lim x->∞ (√(x² + 3x) - x).", "opts": {"a": "3/2", "b": "0", "c": "∞", "d": "3"}, "ans": "a"},
        {"q": "Find the value of k that makes f(x) continuous everywhere, where f(x) = x² - 1 for x < 2, and f(x) = kx + 1 for x >= 2.", "opts": {"a": "1", "b": "2", "c": "3", "d": "0"}, "ans": "a"},
        {"q": "Evaluate the indefinite integral: integral of x * e^(x²) dx.", "opts": {"a": "1/2 * e^(x²) + C", "b": "e^(x²) + C", "c": "2e^(x²) + C", "d": "1/2 * x² * e^(x²) + C"}, "ans": "a"},
        {"q": "Evaluate the indefinite integral: integral of ln(x) dx using integration by parts.", "opts": {"a": "x ln(x) - x + C", "b": "1/x + C", "c": "x ln(x) + C", "d": "1/2 (ln(x))² + C"}, "ans": "a"},
        {"q": "Evaluate the definite integral: integral from 0 to 1 of x * √(1 - x²) dx.", "opts": {"a": "1/3", "b": "2/3", "c": "1/2", "d": "1/4"}, "ans": "a"},
        {"q": "Find the area of the region bounded by the curves y = x² and y = x.", "opts": {"a": "1/6", "b": "1/3", "c": "1/12", "d": "1/2"}, "ans": "a"},
        {"q": "Find the area of the region bounded by the curve y = 4 - x² and the x-axis.", "opts": {"a": "32/3", "b": "16/3", "c": "8", "d": "12"}, "ans": "a"},
        {"q": "Evaluate: integral of x * cos(x) dx using integration by parts.", "opts": {"a": "x sin(x) + cos(x) + C", "b": "x sin(x) - cos(x) + C", "c": "-x cos(x) + sin(x) + C", "d": "x cos(x) + sin(x) + C"}, "ans": "a"},
        {"q": "Evaluate the definite integral: integral from 0 to π/4 of tan(x) dx.", "opts": {"a": "1/2 * ln(2)", "b": "ln(√2)", "c": "ln(2)", "d": "both a and b are correct"}, "ans": "d"},
        {"q": "Evaluate the integral: integral of (2x + 1) / (x² + x + 5) dx.", "opts": {"a": "ln(x² + x + 5) + C", "b": "2 ln(x² + x + 5) + C", "c": "1 / (x² + x + 5) + C", "d": "ln|2x + 1| + C"}, "ans": "a"},
        {"q": "Find the value of: lim x->3 [ (1/x - 1/3) / (x - 3) ].", "opts": {"a": "-1/9", "b": "1/9", "c": "0", "d": "undefined"}, "ans": "a"},
        {"q": "Evaluate: lim x->0 (tan(3x) / sin(5x)).", "opts": {"a": "3/5", "b": "5/3", "c": "1", "d": "0"}, "ans": "a"},
        {"q": "Evaluate the limit: lim x->∞ [ (2x³ - x² + 10) / (5x³ + 2x - 3) ].", "opts": {"a": "2/5", "b": "5/2", "c": "0", "d": "∞"}, "ans": "a"},
        {"q": "Find the area of the region bounded by y = sin(x) and the x-axis from x = 0 to x = 2π.", "opts": {"a": "4", "b": "0", "c": "2", "d": "8"}, "ans": "a"},
        {"q": "Evaluate: integral of sin²(x) dx. Hint: Use half-angle formula.", "opts": {"a": "1/2 * x - 1/4 * sin(2x) + C", "b": "1/2 * x + 1/4 * sin(2x) + C", "c": "-1/3 * sin³(x) + C", "d": "1/2 * x - 1/2 * cos(2x) + C"}, "ans": "a"},
        {"q": "Evaluate: integral of cos²(x) dx. Hint: Use half-angle formula.", "opts": {"a": "1/2 * x + 1/4 * sin(2x) + C", "b": "1/2 * x - 1/4 * sin(2x) + C", "c": "1/3 * cos³(x) + C", "d": "1/2 * x + 1/2 * cos(2x) + C"}, "ans": "a"},
        {"q": "Solve the differential equation: dy/dx = y, given y(0) = 3.", "opts": {"a": "y = 3e^x", "b": "y = e^(3x)", "c": "y = x + 3", "d": "y = 3x"}, "ans": "a"},
        {"q": "Solve the differential equation: dy/dx = 2xy, given y(0) = 5.", "opts": {"a": "y = 5e^(x²)", "b": "y = e^(2x) + 4", "c": "y = 5x²", "d": "y = 5e^(2x)"}, "ans": "a"},
        {"q": "Find the average value of the function f(x) = x² on the interval [0, 3].", "opts": {"a": "3", "b": "9", "c": "4.5", "d": "1"}, "ans": "a"},
        {"q": "Evaluate: integral from -1 to 1 of |x| dx.", "opts": {"a": "1", "b": "0", "c": "2", "d": "1/2"}, "ans": "a"},
        {"q": "Find the limit: lim x->0 [ (cos(2x) - 1) / (cos(x) - 1) ].", "opts": {"a": "4", "b": "2", "c": "0", "d": "undefined"}, "ans": "a"},
        {"q": "Evaluate the definite integral: integral from 0 to 3 of (1 / √(x + 1)) dx.", "opts": {"a": "2", "b": "4", "c": "1", "d": "3"}, "ans": "a"},
        {"q": "Evaluate: integral of x * √(x - 1) dx using substitution u = x - 1.", "opts": {"a": "2/5 (x-1)^(5/2) + 2/3 (x-1)^(3/2) + C", "b": "2/5 (x-1)^(5/2) - 2/3 (x-1)^(3/2) + C", "c": "2/3 (x-1)^(3/2) + C", "d": "x/2 (x-1)² + C"}, "ans": "a"},
        {"q": "Find the limit: lim x->1 (ln(x) / (x - 1)).", "opts": {"a": "1", "b": "0", "c": "e", "d": "undefined"}, "ans": "a"},
        {"q": "Evaluate the integral: integral of dx / (x² - 9). Hint: Use partial fractions.", "opts": {"a": "1/6 * ln|(x - 3)/(x + 3)| + C", "b": "1/6 * ln|(x + 3)/(x - 3)| + C", "c": "1/3 * arctan(x/3) + C", "d": "ln|x² - 9| + C"}, "ans": "a"},
        {"q": "Evaluate the integral: integral of dx / (x² + 9). Hint: Use arctan formula.", "opts": {"a": "1/3 * arctan(x/3) + C", "b": "1/9 * arctan(x/3) + C", "c": "arctan(x/3) + C", "d": "1/3 * ln|x² + 9| + C"}, "ans": "a"},
        {"q": "Find the limit: lim x->0 [ (x - sin(x)) / x³ ]. Hint: Use L'Hopital's rule three times.", "opts": {"a": "1/6", "b": "0", "c": "1/3", "d": "1"}, "ans": "a"},
        {"q": "Evaluate: integral of xe^(-x) dx.", "opts": {"a": "-xe^(-x) - e^(-x) + C", "b": "-xe^(-x) + e^(-x) + C", "c": "xe^(-x) - e^(-x) + C", "d": "1/2 * x² * e^(-x) + C"}, "ans": "a"},
        {"q": "Find the area under the curve y = 1/x from x = 1 to x = e².", "opts": {"a": "2", "b": "1", "c": "e² - 1", "d": "e"}, "ans": "a"},
        {"q": "Solve the differential equation: dy/dx = x/y, with y(0) = 2.", "opts": {"a": "y = √(x² + 4)", "b": "y = x² + 2", "c": "y = √(x² + 2)", "d": "y = x + 2"}, "ans": "a"}
    ]
    return easy, medium, hard

def main():
    seed_file_path = 'lib/services/seed_data.dart'
    
    # 1. Read seed_data.dart
    with open(seed_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx_raw = content.find(start_str)
    if start_idx_raw == -1:
        print("Could not find fullSeedJson")
        return
        
    start_idx = content.find('{', start_idx_raw)
    end_idx = content.rfind("''';")
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find JSON bounds")
        return
        
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    # 2. Add Math Subject
    subjects = data.get('subjects', [])
    # Remove existing math to avoid duplicates if rerun
    subjects = [s for s in subjects if s['id'] != 'math']
    subjects.append({
        'name': 'Mathematics',
        'id': 'math'
    })
    data['subjects'] = subjects
    
    # 3. Add Chapters (Somalia Curriculum)
    chapters = data.get('chapters', [])
    # Remove existing math chapters
    chapters = [c for c in chapters if c['subjectId'] != 'math']
    
    new_chapters = [
        {'subjectId': 'math', 'title': 'Chapter 1: Circular Functions and Trigonometry', 'id': 'math_ch1'},
        {'subjectId': 'math', 'title': 'Chapter 2: Coordinate Geometry (Analytic Geometry)', 'id': 'math_ch2'},
        {'subjectId': 'math', 'title': 'Chapter 3: Geometry and Vectors', 'id': 'math_ch3'},
        {'subjectId': 'math', 'title': 'Chapter 4: Probability', 'id': 'math_ch4'},
        {'subjectId': 'math', 'title': 'Chapter 5: Complex Numbers', 'id': 'math_ch5'},
        {'subjectId': 'math', 'title': 'Chapter 6: Differentiation (Calculus)', 'id': 'math_ch6'},
        {'subjectId': 'math', 'title': 'Chapter 7: Limits, Continuity and Integration (Calculus)', 'id': 'math_ch7'},
    ]
    
    chapters.extend(new_chapters)
    data['chapters'] = chapters
    
    # 4. Generate Questions for each of the 7 chapters (Somalia Curriculum)
    all_questions = []
    
    ch_generators = {
        1: create_ch1_questions,
        2: create_ch2_questions,
        3: create_ch3_questions,
        4: create_ch4_questions,
        5: create_ch5_questions,
        6: create_ch6_questions,
        7: create_ch7_questions,
    }
    
    for ch_num in range(1, 8):
        easy_b, med_b, hard_b = ch_generators[ch_num]()
        
        # Verify sizes
        if len(easy_b) < 25 or len(med_b) < 29 or len(hard_b) < 32:
            print(f"Error: Chapter {ch_num} has insufficient questions! Easy: {len(easy_b)}, Medium: {len(med_b)}, Hard: {len(hard_b)}")
            return
            
        ch_id = f"math_ch{ch_num}"
        
        # Take exactly the requested counts
        # Easy: 25
        for i in range(25):
            bq = easy_b[i]
            all_questions.append({
                "id": f"Math_Ch{ch_num}_Q{str(i+1).zfill(2)}",
                "question": bq["q"],
                "options": bq["opts"],
                "correctAnswer": bq["ans"],
                "difficultyLevel": "easy",
                "subjectId": "math",
                "chapterId": ch_id
            })
            
        # Medium: 29
        for i in range(29):
            bq = med_b[i]
            all_questions.append({
                "id": f"Math_Ch{ch_num}_Q{str(i+26).zfill(2)}",
                "question": bq["q"],
                "options": bq["opts"],
                "correctAnswer": bq["ans"],
                "difficultyLevel": "medium",
                "subjectId": "math",
                "chapterId": ch_id
            })
            
        # Hard: 32
        for i in range(32):
            bq = hard_b[i]
            all_questions.append({
                "id": f"Math_Ch{ch_num}_Q{str(i+55).zfill(2)}",
                "question": bq["q"],
                "options": bq["opts"],
                "correctAnswer": bq["ans"],
                "difficultyLevel": "hard",
                "subjectId": "math",
                "chapterId": ch_id
            })
            
    # 5. Merge new questions
    questions = data.get('questions', [])
    # Remove existing math questions
    questions = [q for q in questions if q.get('subjectId') != 'math']
    questions.extend(all_questions)
    data['questions'] = questions
    
    # 6. Write back to seed_data.dart
    updated_json = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content[:start_idx] + updated_json + "\n" + content[end_idx:]
    
    with open(seed_file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully generated {len(all_questions)} questions for Mathematics subject (7 chapters) and merged them into seed_data.dart!")

if __name__ == '__main__':
    main()
