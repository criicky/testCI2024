# Dataset 4

| Run | GP Formula | GP Train Fitness | GP Test Fitness | MC Formula | MC Train Fitness | MC Test Fitness |
|-----|------------|------------------|-----------------|------------|------------------|-----------------|
| 1 | protected_log10(square(square(protected_log2(protected_divide(protected_log(protected_log10(maximum(maximum(protected_power(1.618033988749895, exp(0.5)), square(cbrt(x[1]))), protected_divide(multiply(0.5, 0.6931471805599453), cos(x[1]))))), cos(x[1])))))) | 2.457394e+00 | 2.514593e+00 | add(add(multiply(2.0, add(cos(x[1]), protected_power(1.618033988749895, cos(x[1])))), cos(x[1])), add(add(add(cbrt(maximum(protected_power(protected_log2(1.7320508075688772), protected_divide(subtract(x[0], 1.7320508075688772), tanh(cosh(add(x[0], 0.0))))), arctan(cos(-1.0)))), cos(x[1])), cos(x[1])), cos(x[1]))) | 8.187952e-03 | 8.414143e-03 |
| 2 | subtract(tan(cos(subtract(sin(sin(exp(exp(protected_power(cosh(protected_mod(1.618033988749895, 0.5)), minimum(add(1.4142135623730951, x[0]), cbrt(x[0]))))))), sinh(maximum(multiply(protected_log2(1.7320508075688772), cos(arctan(protected_sqrt(reciprocal(x[0]))))), 0.6931471805599453))))), subtract(subtract(protected_divide(cos(x[1]), subtract(sinh(arccos(protected_log2(1.7320508075688772))), sin(absolute(2.0)))), cos(protected_divide(subtract(maximum(cbrt(add(protected_log10(tan(1.0)), x[0])), protected_power(cosh(protected_log2(1.7320508075688772)), minimum(tanh(add(2.302585092994046, x[0])), protected_log10(absolute(x[0]))))), cos(x[1])), add(sinh(maximum(sin(minimum(add(1.618033988749895, 1.7320508075688772), x[0])), negative(tanh(cos(x[1]))))), cosh(cbrt(add(protected_log10(1.618033988749895), x[0]))))))), subtract(1.618033988749895, subtract(subtract(tanh(sin(sin(arccos(protected_log2(1.7320508075688772))))), cos(x[1])), cos(x[1]))))) | 1.525073e-03 | 1.550844e-03 | add(add(cos(x[1]), add(arccos(protected_mod(tanh(add(add(0.5, protected_mod(cos(protected_divide(3.141592653589793, x[0])), protected_sqrt(2.718281828459045))), x[0])), 0.5)), cos(x[1]))), add(add(add(add(cos(x[1]), add(cos(x[1]), 2.0)), cos(x[1])), cos(x[1])), cos(x[1]))) | 9.841724e-03 | 9.899447e-03 |
| 3 | add(add(add(cos(add(cos(protected_divide(protected_divide(arccos(cos(x[1])), tanh(2.0)), tanh(arccos(cos(x[1]))))), cos(x[1]))), absolute(absolute(add(cos(arccos(cos(x[1]))), exp(cos(arctan(x[1]))))))), add(cos(arccos(cos(arccos(cos(arccos(cos(x[1]))))))), cos(protected_divide(arccos(cos(protected_divide(x[1], tanh(tan(2.0))))), tanh(cosh(subtract(minimum(subtract(x[0], x[0]), protected_mod(protected_divide(x[0], 2.0), x[0])), tanh(tanh(absolute(x[1])))))))))), add(add(exp(cos(arccos(cos(arccos(cos(x[1])))))), cos(maximum(protected_divide(arccos(cos(arccos(cos(x[1])))), tanh(cosh(subtract(2.302585092994046, minimum(2.0, cbrt(x[0])))))), tanh(subtract(x[0], arccos(cos(x[1]))))))), cos(arccos(cos(protected_divide(x[1], tanh(2.0))))))) | 2.860253e-02 | 2.948246e-02 | add(add(cos(x[1]), add(protected_divide(x[0], protected_log10(protected_power(protected_divide(x[0], cosh(protected_divide(square(1.0), protected_power(add(2.0, 0.5), subtract(0.0, 2.718281828459045))))), 2.302585092994046))), add(cos(x[1]), add(negative(0.6931471805599453), add(add(add(add(cos(x[1]), 2.0), cos(x[1])), cos(x[1])), cos(x[1])))))), add(cos(x[1]), 2.0)) | 3.298390e-04 | 3.361781e-04 |
| 4 | add(add(cbrt(add(tanh(1.7320508075688772), protected_power(1.0, add(multiply(cos(reciprocal(arccos(protected_log(x[0])))), cos(minimum(x[1], cos(x[1])))), cos(x[1]))))), add(add(add(2.302585092994046, add(cos(x[1]), cos(x[1]))), minimum(multiply(protected_sqrt(protected_power(cbrt(2.718281828459045), 2.0)), add(add(cos(cos(x[1])), cos(x[1])), 2.0)), multiply(2.0, cos(x[1])))), cos(x[1]))), minimum(minimum(2.0, multiply(protected_sqrt(protected_power(cbrt(cbrt(cbrt(1.4142135623730951))), cos(x[1]))), add(multiply(cbrt(add(3.141592653589793, x[0])), minimum(multiply(cbrt(add(add(0.6931471805599453, x[0]), x[0])), minimum(protected_log10(1.4142135623730951), cos(1.7320508075688772))), cos(1.7320508075688772))), multiply(2.0, cos(x[1]))))), multiply(add(add(2.302585092994046, add(cos(cos(1.7320508075688772)), cos(minimum(cos(1.7320508075688772), cos(x[1]))))), minimum(2.718281828459045, multiply(multiply(cos(cos(x[1])), multiply(cos(cos(2.302585092994046)), cos(x[1]))), subtract(cbrt(2.718281828459045), protected_log10(add(square(add(3.141592653589793, x[0])), subtract(sinh(x[0]), 1.7320508075688772))))))), minimum(multiply(add(cos(x[1]), cos(cbrt(2.718281828459045))), protected_sqrt(add(multiply(cos(cbrt(3.141592653589793)), cos(cos(1.7320508075688772))), cos(cbrt(cbrt(2.0)))))), cos(cos(1.7320508075688772)))))) | 1.824909e-03 | 1.846764e-03 | add(maximum(protected_sqrt(maximum(3.141592653589793, subtract(cosh(1.618033988749895), add(x[0], multiply(cosh(1.618033988749895), multiply(cos(3.141592653589793), cosh(1.618033988749895))))))), 3.141592653589793), multiply(multiply(cosh(1.618033988749895), cos(x[1])), cosh(1.618033988749895))) | 2.585639e-02 | 2.530149e-02 |

<table><tr><th>GP Run 1</th><th>MC Run 1</th></tr>
<tr><td><img src='ds4_GP_run1_tree.png' width='320'><br>Tree</td><td><img src='ds4_MC_run1_tree.png' width='320'><br>Tree</td></tr>
<tr><td><img src='ds4_GP_run1_fitness.png' width='320'><br>Fitness</td><td><img src='ds4_MC_run1_fitness.png' width='320'><br>Fitness</td></tr>
<tr><td><img src='ds4_GP_run1_pred.png' width='320'><br>Prediction</td><td><img src='ds4_MC_run1_pred.png' width='320'><br>Prediction</td></tr>
</table>

<table><tr><th>GP Run 2</th><th>MC Run 2</th></tr>
<tr><td><img src='ds4_GP_run2_tree.png' width='320'><br>Tree</td><td><img src='ds4_MC_run2_tree.png' width='320'><br>Tree</td></tr>
<tr><td><img src='ds4_GP_run2_fitness.png' width='320'><br>Fitness</td><td><img src='ds4_MC_run2_fitness.png' width='320'><br>Fitness</td></tr>
<tr><td><img src='ds4_GP_run2_pred.png' width='320'><br>Prediction</td><td><img src='ds4_MC_run2_pred.png' width='320'><br>Prediction</td></tr>
</table>

<table><tr><th>GP Run 3</th><th>MC Run 3</th></tr>
<tr><td><img src='ds4_GP_run3_tree.png' width='320'><br>Tree</td><td><img src='ds4_MC_run3_tree.png' width='320'><br>Tree</td></tr>
<tr><td><img src='ds4_GP_run3_fitness.png' width='320'><br>Fitness</td><td><img src='ds4_MC_run3_fitness.png' width='320'><br>Fitness</td></tr>
<tr><td><img src='ds4_GP_run3_pred.png' width='320'><br>Prediction</td><td><img src='ds4_MC_run3_pred.png' width='320'><br>Prediction</td></tr>
</table>

<table><tr><th>GP Run 4</th><th>MC Run 4</th></tr>
<tr><td><img src='ds4_GP_run4_tree.png' width='320'><br>Tree</td><td><img src='ds4_MC_run4_tree.png' width='320'><br>Tree</td></tr>
<tr><td><img src='ds4_GP_run4_fitness.png' width='320'><br>Fitness</td><td><img src='ds4_MC_run4_fitness.png' width='320'><br>Fitness</td></tr>
<tr><td><img src='ds4_GP_run4_pred.png' width='320'><br>Prediction</td><td><img src='ds4_MC_run4_pred.png' width='320'><br>Prediction</td></tr>
</table>


---

