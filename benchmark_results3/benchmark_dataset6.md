# Dataset 6

| Run | GP Formula | GP Train Fitness | GP Test Fitness | MC Formula | MC Train Fitness | MC Test Fitness |
|-----|------------|------------------|-----------------|------------|------------------|-----------------|
| 1 | add(minimum(maximum(x[1], protected_divide(subtract(subtract(x[1], x[0]), -1.0), protected_divide(0.5, protected_mod(cbrt(protected_log10(sin(1.0))), maximum(0.6931471805599453, add(minimum(1.4142135623730951, protected_log2(x[1])), protected_log10(sin(1.0)))))))), minimum(maximum(minimum(-1.0, tanh(x[0])), protected_divide(subtract(subtract(x[1], add(-1.0, sin(negative(1.618033988749895)))), x[0]), protected_divide(exp(tanh(add(add(-1.0, -1.0), add(-1.0, 1.0)))), protected_mod(cbrt(protected_log10(sin(1.0))), maximum(0.6931471805599453, cos(1.4142135623730951)))))), protected_divide(subtract(x[1], x[0]), protected_divide(exp(tanh(negative(1.7320508075688772))), protected_mod(cbrt(protected_log10(sin(protected_power(protected_power(3.141592653589793, x[0]), tan(3.141592653589793))))), maximum(0.6931471805599453, cos(1.4142135623730951))))))), x[1]) | 2.434874e-08 | 2.357089e-08 | subtract(multiply(protected_log2(maximum(maximum(3.141592653589793, protected_log(protected_log(protected_power(2.0, x[0])))), exp(sinh(1.0)))), x[1]), protected_log(protected_power(2.0, x[0]))) | 1.159943e-05 | 1.200318e-05 |
| 2 | add(add(add(protected_divide(x[0], 3.141592653589793), x[1]), protected_log2(cos(arcsin(subtract(cos(protected_mod(tanh(minimum(1.4142135623730951, x[1])), sin(sin(minimum(1.0, x[1]))))), cos(tanh(multiply(x[1], protected_power(cbrt(0.5), 1.0))))))))), add(subtract(subtract(arctan(cos(protected_power(tanh(2.302585092994046), subtract(2.718281828459045, x[0])))), x[0]), cos(subtract(add(add(-1.0, multiply(sin(sin(2.718281828459045)), multiply(minimum(1.618033988749895, x[1]), tanh(multiply(3.141592653589793, 0.6931471805599453))))), multiply(x[1], tanh(2.718281828459045))), minimum(protected_power(protected_power(2.718281828459045, 0.6931471805599453), 0.6931471805599453), minimum(1.618033988749895, x[1]))))), x[1])) | 2.928561e-04 | 3.012573e-04 | subtract(subtract(multiply(x[1], exp(0.5)), protected_log10(cosh(maximum(x[0], arctan(multiply(0.5, exp(0.5))))))), arctan(multiply(x[0], multiply(0.5, maximum(1.7320508075688772, arctan(x[0])))))) | 2.972989e-02 | 3.074304e-02 |
| 3 | add(subtract(x[1], arctan(add(arctan(multiply(multiply(protected_power(tanh(1.4142135623730951), cbrt(multiply(x[0], multiply(2.302585092994046, x[1])))), x[0]), tan(tan(0.5)))), subtract(x[1], arctan(add(maximum(x[1], negative(add(square(x[1]), maximum(x[0], 0.0)))), arctan(minimum(multiply(arctan(x[0]), cosh(x[1])), maximum(x[0], 0.0))))))))), subtract(x[1], multiply(tan(tan(0.5)), multiply(protected_power(tanh(3.141592653589793), add(maximum(multiply(sin(x[1]), multiply(exp(1.4142135623730951), multiply(2.0, x[1]))), negative(maximum(multiply(x[0], sinh(x[1])), x[0]))), multiply(exp(maximum(sin(x[0]), multiply(-1.0, exp(1.4142135623730951)))), exp(sin(x[1]))))), multiply(multiply(protected_power(tanh(3.141592653589793), cbrt(multiply(protected_log(arccos(x[1])), maximum(x[0], x[1])))), x[0]), protected_power(tanh(maximum(square(1.7320508075688772), x[0])), maximum(cbrt(multiply(square(x[1]), x[0])), multiply(sin(x[1]), multiply(exp(1.4142135623730951), multiply(2.0, x[1])))))))))) | 4.301768e-03 | 4.185218e-03 | protected_divide(minimum(maximum(subtract(x[1], reciprocal(protected_divide(x[1], x[0]))), 2.302585092994046), subtract(x[1], reciprocal(protected_divide(add(negative(tan(protected_power(2.718281828459045, tan(subtract(0.0, 2.302585092994046))))), 2.302585092994046), x[0])))), sinh(sinh(cos(-1.0)))) | 2.839983e-03 | 2.835116e-03 |
| 4 | subtract(x[1], protected_mod(protected_power(subtract(protected_mod(minimum(tanh(minimum(2.718281828459045, x[1])), cbrt(reciprocal(protected_divide(cosh(x[0]), multiply(2.718281828459045, x[0]))))), protected_mod(cosh(multiply(1.618033988749895, cbrt(subtract(add(2.0, 1.0), subtract(x[1], 0.5))))), multiply(cosh(negative(protected_divide(x[0], cos(1.618033988749895)))), multiply(minimum(2.718281828459045, subtract(x[1], x[0])), subtract(exp(x[1]), protected_power(arctan(x[1]), protected_divide(1.4142135623730951, 1.0))))))), cosh(protected_sqrt(subtract(sinh(minimum(subtract(x[0], x[1]), x[1])), multiply(cbrt(maximum(protected_mod(x[1], 2.718281828459045), multiply(x[1], x[1]))), negative(maximum(2.718281828459045, multiply(x[0], x[1])))))))), -1.0), subtract(protected_divide(tanh(minimum(x[0], protected_power(cosh(maximum(protected_divide(protected_log10(x[1]), cbrt(x[1])), 1.0)), exp(subtract(x[1], add(cos(x[0]), 0.5)))))), minimum(cbrt(reciprocal(cosh(x[0]))), maximum(protected_divide(reciprocal(negative(x[0])), maximum(tanh(subtract(protected_divide(3.141592653589793, 1.4142135623730951), 1.0)), 0.6931471805599453)), add(negative(protected_divide(x[0], cos(1.618033988749895))), negative(protected_divide(x[0], cos(1.618033988749895))))))), x[1]))) | 3.578063e-02 | 3.897990e-02 | add(multiply(negative(x[0]), multiply(protected_log10(negative(multiply(1.618033988749895, tan(-1.0)))), 1.7320508075688772)), add(x[1], multiply(x[1], 0.6931471805599453))) | 1.094628e-05 | 1.056191e-05 |

<table><tr><th>GP Run 1</th><th>MC Run 1</th></tr>
<tr><td><img src='ds6_GP_run1_tree.png' width='320'><br>Tree</td><td><img src='ds6_MC_run1_tree.png' width='320'><br>Tree</td></tr>
<tr><td><img src='ds6_GP_run1_fitness.png' width='320'><br>Fitness</td><td><img src='ds6_MC_run1_fitness.png' width='320'><br>Fitness</td></tr>
<tr><td><img src='ds6_GP_run1_pred.png' width='320'><br>Prediction</td><td><img src='ds6_MC_run1_pred.png' width='320'><br>Prediction</td></tr>
</table>

<table><tr><th>GP Run 2</th><th>MC Run 2</th></tr>
<tr><td><img src='ds6_GP_run2_tree.png' width='320'><br>Tree</td><td><img src='ds6_MC_run2_tree.png' width='320'><br>Tree</td></tr>
<tr><td><img src='ds6_GP_run2_fitness.png' width='320'><br>Fitness</td><td><img src='ds6_MC_run2_fitness.png' width='320'><br>Fitness</td></tr>
<tr><td><img src='ds6_GP_run2_pred.png' width='320'><br>Prediction</td><td><img src='ds6_MC_run2_pred.png' width='320'><br>Prediction</td></tr>
</table>

<table><tr><th>GP Run 3</th><th>MC Run 3</th></tr>
<tr><td><img src='ds6_GP_run3_tree.png' width='320'><br>Tree</td><td><img src='ds6_MC_run3_tree.png' width='320'><br>Tree</td></tr>
<tr><td><img src='ds6_GP_run3_fitness.png' width='320'><br>Fitness</td><td><img src='ds6_MC_run3_fitness.png' width='320'><br>Fitness</td></tr>
<tr><td><img src='ds6_GP_run3_pred.png' width='320'><br>Prediction</td><td><img src='ds6_MC_run3_pred.png' width='320'><br>Prediction</td></tr>
</table>

<table><tr><th>GP Run 4</th><th>MC Run 4</th></tr>
<tr><td><img src='ds6_GP_run4_tree.png' width='320'><br>Tree</td><td><img src='ds6_MC_run4_tree.png' width='320'><br>Tree</td></tr>
<tr><td><img src='ds6_GP_run4_fitness.png' width='320'><br>Fitness</td><td><img src='ds6_MC_run4_fitness.png' width='320'><br>Fitness</td></tr>
<tr><td><img src='ds6_GP_run4_pred.png' width='320'><br>Prediction</td><td><img src='ds6_MC_run4_pred.png' width='320'><br>Prediction</td></tr>
</table>


---

