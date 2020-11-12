<h1>Telegram BOT - ТС и ТЭДС(@TR100Bot - в разработке)</h1>
<h2>Отношения сопротивлений для ТС и ЧЭ: медных, платиновых, никелевых. Значениея ТЭДС термопар типов R, S, В, J, Т, Е, К, N, A, L, М.</h2>

<h3>Список задач</h3>

- [X] Дописать основные файлы
- [ ] Проверить точность
- [ ] Протестировать
- [ ] Отправить на VPS

<h3>Файлы</h3>

<p>
:white_check_mark: main_bot — бот<br>
:white_check_mark: <b>custom_req_hundler</b> — обработка сообщений<br>
:white_check_mark: <b>main_polinom.py</b> — рассчеты полиномов в зависимости от типа ТП и значения<br>
:white_check_mark: <b>main_intplt_equations.py</b> — интерполяцилнные уравнения для Cu, Ni, Pt термометров сопротивления в зависимости от типа и значения<br>
:white_check_mark: <b>coefficients.py</b> — коэффициенты ТП<br>
:white_check_mark: <b>extracting_coefficients_mV.py</b> — вычисление коэффициентов полиномов, аппроксимирующих НСХ преобразования термопар, для случаев неверных данных в ГОСТ Р 8.585-2001<br>
:white_check_mark: <b>extracting_coefficients_T.py</b> — вычисление коэффициентов полиномов, аппроксимирующих обратную зависимость НСХ преобразования (температуры от ТЭДС), для случаев неверных данных в ГОСТ Р 8.585-2001<br>
<b>EDS_mV.txt</b> — табличные значения ТЭДС(mV) по ГОСТ, для требуемого диапазона температур<br>
:black_square_button: <b>user_message.log</b> — лог нераспознанных сообщений
</p>

<h3>Тестирование</h3>

<p>
:black_square_button: <b>test_main.py</b> <br>
</p>
Тестирование преобразуемых значений ТП
<pre>pytest -m tp --reruns 1 -s -v --tb=line test_main.py</pre>
Тестирование преобразуемых значений ТСМ
<pre>pytest -m tsm --reruns 1 -s -v --tb=line test_main.py</pre>

<h3>Точность</h3>
<p>
ТСМ(Ом) — 0.00Ом<br>
ТСМ(Т) — 0.0°C
</p>
<p>
ТП(мВ) — 0.00mV<br>
ТП(Т) — 0.0°C
</p>

<h3>Использование</h3>
<p>В чат бота отправить значение и тип ТП или ТСМ.</p>
<p>Целые числа бот распознаёт как значение температуры. Числа с плавающей точкой бот распознаёт как Омы или мВ.
Если требуется указать температуру с плавающей точкой или Омы и мВ целым числом, используйте префиксы t, mV, Ом после значения.</p> 


Т для ТП
<pre>
-5.89 K
вернёт <<i>-200°C (тип K)</i>>
</pre>
<pre>
-5mv K
вернёт <<i>-153.736°C (тип K)</i>>
</pre>

mV для ТП
<pre>
-200 K
вернёт <<i>-5.89mV (тип К)</i>>
</pre>
<pre>
-200.0t K
вернёт <<i>-5.89mV (тип К)</i>>
</pre>

Т для ТСМ
<pre>
74,60 100M
вернёт <<i>-58.9°C (тип Cu85)</i>>
</pre>
<pre>
74r 100M 
вернёт <<i>-60.2°C (тип Cu85)</i>>
</pre>

Ом для ТСМ
<pre>
115 50M
вернёт <<i>74,60Ом (тип Cu85)</i>>
</pre>
<pre>
115.0t 50M
вернёт <<i>74,60Ом (тип Cu85)</i>>
</pre>

<h3>Примчание</h3>

<p>По умолчанию характеристика α:<br>
 </p>

<ul>
  <li>Медные(Cu) - 0.00428</li>
  <li>Платиновые(Pt) - 0.00391</li>
  <li>Никелевые(Ni) - 0.00617</li>
</ul>

Если необходимо изменить эту характеристику, то добавьте требуемое значение в конце сообщения, через пробел. Например, так:
<pre>
-50 50M 426
вернёт <<i>78.70 Ом(Cu426)</i>>
</pre>
<pre>
-50 50M 428
вернёт <<i>78.46 Ом(Cu426)</i>>
</pre>

<p>Допустимые значения для: медных - 426 и 428, платиновых - 385 и 391, никелевых - 617</p>