<h1>Telegram BOT - ТС и ТЭДС</h1>
<h2>Отношения сопротивлений для ТС. ТЭДС термопар типов R, S, В, J, Т, Е, К, N, A, L, М</h2>

<h3>Файлы</h3>
<p>
<b>main_bot</b> — бот<br>
<b>main_polinom.py</b> — рассчет полинома в зависимости от типа ТП и значения<br>
<b>main_intplt_equations.py</b> — интерполяцилнные уравнения для Cu, Ni, Pt термометров сопротивления<br>
<b>coefficients.py</b> — коэффициенты ТП<br>
<b>extracting_coefficients_mV.py</b> — вычисление коэффициентов полиномов, аппроксимирующих НСХ преобразования термопар<br>
<b>extracting_coefficients_T.py</b> — вычисление коэффициентов полиномов, аппроксимирующих обратную зависимость НСХ преобразования (температуры от ТЭДС)<br>
<b>EDS_mV.txt</b> — табличные значения ТЭДС(mV) по ГОСТ, для требуемого диапазона температур
</p>

<h3>Тестирование</h3>
<p>
<b>test_main.py</b> <br>
</p>
Тестирование преобразуемых значений ТП
<pre>pytest -m tp --reruns 1 -s -v --tb=line test_main.py</pre>
Тестирование преобразуемых значений ТСМ
<pre>pytest -m tsm --reruns 1 -s -v --tb=line test_main.py</pre>

<h3>Использование</h3>
<p>
В чат бота отправить тип ТП или ТСМ и значение.
</p>
Т для ТП
<pre>K -5.89
вернёт <-200></pre>
mV для ТП
<pre>K -200
вернёт <-5.89></pre>
Т для ТСМ
<pre>Cu85 74,60
вернёт <115></pre>
Ом для ТСМ
<pre>Cu85 115
вернёт <74,60></pre>
