# rus-dict
The Code for the Bachelor Thesis: "Dictionary of Russian Language of the 11th — 17th Centuries as a Database: Information Retrieval and Research Perspectives"
Создание словаря
#Материалы
Электронная версия Словаря русского языка 11 - 17 веков была создана на основе трех томов словаря, доступных в электронном виде в формате DOC. Были использованы 28 – 30 тома, в которых представлены слова с “Старичекъ” до “Уберечися”. Эти три тома содержат 6306 словарных статей. В словаре для каждого слова представлена такая информация, как его частеречная принадлежность, определение, примеры употребления. Для каждого примера также указана дата употребления (век или год) и сокращенное название источника. Также в статьях есть ссылки на иноязычные параллели и на другие слова из словаря.
Стоит упомянуть, что версия словаря, на основе которой создавалась база данных, не является финальной версией, которая была издана и существует в бумажном варианте. В текст словаря, который использовался в этой работе, не были внесены исправления, которые присутствуют в бумажной версии словаря.
Для создания электронной версии словаря также использовался список источников цитатного материала, использованного для иллюстрации употребления слов в статьях. В списке представлена основная информация по каждому источнику, такая, как полное название источника, список сокращенных названий, которые использовались для указания на источник в тексте словаря, дата создания текста, дата создания списка. Также в этом списке представлена классификация источников по жанрам. Всего в этом списке представлено 3032 источника, однако не все из них расклассифицированы по жанрам. На данный момент расклассифицировано 900 источников. 
##Метод
Для того, чтобы создать электронный вариант Словаря русского языка XI - XVII веков было необходимо представить текст (в формате DOC) трех использованных томов в структурированном виде. Это позволило создать поиск по разным полям словарных статей.  Для этого было необходимо решить следующие задачи: препроцессинг исходного текста, разбиение текста на словарные статьи, разбиение текста каждой статьи на функциональные зоны, создание базы данных, создание интерфейса для поиска по полученной базе.
###Препроцессинг
Первая проблема, которую было необходимо решить, была связана со шрифтами, использовавшимися при наборе текста словаря. В тексте словаря для отображения древнерусских символов был использован шрифт KDRS. С его помощью передавались такие символы как «ѣ», «Ѣ» (ять) и « ҃ » (титло). Однако, чтобы символы отображались правильно, шрифт KDRS нужно специально скачать и установить, так как он отсутствует на большинстве компьютеров. Таким образом, при отсутствии нужного шрифта символ «ѣ» отображался как «#», «Ѣ» - как «@», а « ҃ » - как «%». Такая же проблема была связана со всеми греческими символами, которые использовались для передачи иноязычных параллелей греческого языка в тексте словарных статей. Для отображения греческих символов был использован шрифт Hellenica, который, так же, как и KDRS, нужно специально скачать и установить. При этом в случае, если шрифт не установлен, все греческие символы отображаются неверно. Проблема шрифтов была решена заменой всех символов, отображающихся неверно, на соответствующие им символы из таблицы Unicode, благодаря чему они отображаются верно при использовании практически любого шрифта. 
Следующая проблема состояла в том, что набранный текст словаря был в формате DOC. Этот формат является удобным для и ориентированным на пользователя, но текст в этом формате проблематично обрабатывать при помощи любых программ, кроме Microsoft Word и его аналогов. Однако функций MS Word было недостаточно для того, чтобы осуществить обработку текста, необходимую для представления текста в структурированном виде. Таким образом, необходимо было перевести текст в формат, который можно легко использовать при обработке текста без помощи MS Word. При этом необходимо было сохранить оформление, использованное в тексте словаря (полужирный шрифт, курсив), так как оно отражает структуру каждой словарной статьи, и именно благодаря этому оформлению было возможно автоматически разделить статьи на функциональные зоны. Решением этой задачи стал перевод текста в формат языка гипертекстовой разметки HTML. Текст в этом формате можно автоматически обработать при помощи практически любой программы, также он позволил сохранить оформление текста, представив его в виде тегов.
###Разбиение текста на словарные статьи
Для разбиения текста словаря на словарные статьи использовался скрипт, написанный на языке программирования Python. Каждая словарная статья начинается с нового абзаца. В том случае, если у заголовочного слова есть только одно значение, конец абзаца маркирует конец словарной статьи. В случае, если у заголовочного слова несколько значений, каждое значение оформляется в отдельный абзац. Заголовочное слово, которое находится в начале каждой словарной статьи оформляется полужирным шрифтом и пишется заглавными буквами. Таким образом, начало нового абзаца с набора символов, являющихся заглавными буквами и оформленных полужирным шрифтом, маркирует начало новой словарной статьи. 
Для разбиения текста на словарные статьи был написан скрипт на Python с использованием регулярных выражений. Результатом его работы был список словарных статей словаря. 
###Разбиение статей на функциональные зоны
После того, как был получен список словарных статей, было необходимо разбить каждую статью на функциональные зоны. В большинстве словарных статей были выделены следующие зоны: заголовочное слово, грамматические пометы, определение, примеры употребление, источник, дата употребления. В случае, если есть несколько значений, оно содержит несколько определений. У каждого значения есть свой набор примеров. Значение слова может иллюстрироваться как одним примером, так и несколькими. Для каждого примера указывается дата и источник. Далее приведен пример того, как выглядит подобная словарная статья.


	Кроме того, словарная статья может содержать ссылки на другие статьи. Они также выделялись в отдельное поле.
	В словаре также присутствуют словарные статьи в которых содержится только ссылка на другую статью.
	
Такая статья содержит только два функциональных поля: заголовочное слово и ссылка.
Для того, чтобы автоматически поделить словарные статьи на зоны, был написан скрипт на Python с использованием как регулярных выражений и конечных автоматов. Скрипт доступен на GitHub по ссылке: https://github.com/AnnaVechkaeva/RusDict/blob/master/DB_creation/article_div.py 
###Создание базы данных
После того, как все словарные статьи были поделены на функциональные зоны, было необходимо организовать всю извлеченную информацию в базу данных, которая содержит всю извлеченную информацию и делает возможным поиск по ней. Была использована база данных SQL. Для создания базы данных был использован язык программирования Python и модуль sqlite3. Использованный скрипт доступен на GitHub по ссылке: https://github.com/AnnaVechkaeva/RusDict/blob/master/DB_creation/insert_DB.py 
Структура словарной статьи Словаря русского языка XI – XVII веков делает непрактичным использование для хранения информации из словаря в базе данных только одной таблицы, так как одному заголовочному слову могут соответствовать несколько значений, а одно значение в свою очередь в большинстве случаев иллюстрируется несколькими примерами. Организовать информацию с подобной структурой в одной таблице можно одним из двух следующих способов, каждый из которых имеет свои недостатки. 
При использовании первого способа каждому заголовочному слову соответствует одна строка в таблице. При этом определения всех значений слова записываются в одну ячейку, все примеры для приведенные для иллюстрации употребления слова – во вторую, названия всех источников, упомянутых в словарной статье – в третью, а все даты, присутствующие в статье – в четвертую. Таким образом словарная статья для слова «старожилец», статья которого приведена ниже, организованная подобным образом, будет выглядеть, как показано в таблице 2.
 
При этом, если по таблице, организованной таким образом, осуществлять поиск по какому-либо одному параметру, то он будет работать правильно. Однако если поиск будет осуществляться по двум параметрам, описывающим примеры (например, по тексту примера и по дате упоминания), то возникнут проблемы, так как при такой структуре таблицы невозможно установить соответствие между примером, его источником и датой. При таком поиске по этой таблице результаты будут выдаваться неправильно. Так, например, когда пользователь хочет найти статью, в тексте примера которой есть слово «тѣм» (первый пример), употребленное в 1652 году, статья слова «старожилецъ» будет получена в качестве результата, хотя она на самом деле не удовлетворяет параметрам, введенным пользователем. 
Второй способ организовать словарную статью в одной таблице – это записывать каждый пример в отдельную ячейку, при этом заголовочное слово будет записано в таблице столько раз, сколько в его статье есть примеров, и определение слова появится столько раз, сколько ему соответствует примеров. 

Таким образом, при использовании второго способа записи данных из словаря в одну таблицу ошибки, которая возникала при использовании первого способа, возникать не будет. Если пользователь будет искать словарную статью, в примерах которой содержится слово «тѣм» (первый пример), употребленное в 1652 году, статьи слова «старожилецъ» не будет среди полученных результатов поиска. Однако и у этого способа есть недостаток. Он заключается в том, что заголовочное слово и определение могут дублироваться в нескольких строках таблицы, что является неэкономным. При этом, если для хранения информации использовать не одну, а три таблицы, то ячейки таблиц не будут дублироваться, и база данных будет занимать меньше памяти. 
Информация, извлеченная из текста словаря, была организована в трех связанных таблицах. В первой таблице содержится основная информация о заголовочном слове: само слово, грамматические пометы и ссылки на другие статьи. Во второй таблице содержатся определения. Третья таблица содержит примеры, иллюстрирующие употребление слов, и информацию о примерах: сокращенное название источника и дата употребления. Кроме того, в базу данных была включена таблица, содержащая информацию об источниках, использовавшихся для цитатного материала. Эта таблица содержит такую информацию, как полное название источника, сокращенное название источника, дата создания списка текста источника, дата создания текста, язык оригинала для переводных источников, а также информацию о жанре источника.

### Создание интерфейса
Для того, чтобы сделать поиск по созданной базе данных удобным и доступным, был создан интерфейс. Для его создания использовался язык HTML и язык программирования Python. Поиск по базе данных осуществляется при помощи модуля sqlite3 при помощи SQL-запросов, которые формируются из параметров, заданных пользователем. Передача параметров поиска и формирование html-страниц происходит при помощи модуля Flask. 
#### Поиск по словарю
Интерфейс для поиска по словарю имеет следующие функции: поиск по заголовочному слову, поиск по маске, поиск по примерам, поиск по части речи, поиск по дате. Кроме того, доступен поиск по словарю с учетом информации из списка источников. Доступны следующие опции: поиск по языку оригинала источника, поиск по жанру источника.
Для поиска по заголовочному слову необходимо ввести в слово целиком. Например, если ввести в это поле «старо», то будет найдена одна статья на слово «старо». 
Поиск по маске позволяет искать статьи по части заголовочного слова. Для этого используется упрощенная версия регулярных выражений. Символ «_» (нижнее подчеркивание) используется для указания на любой символ, а символ «%» - для указания на любое количество символов. Например, если ввести в это поле «стар_», то будет найдено две статьи: для слов «старо» и «старь». А если ввести в это поле «стар%», то при выдаче будут показаны все слова, которые начинаются на «стар».
Поиск по примерам позволяет производить поиск по тексту примеров. Если ввести слово «старо» в это поле, то будут найдены все статьи, в примерах которых встретилось это слово.
Также доступен поиск по части речи. Для поиска необходимо выбрать из списка нужные части речи. В списке представлены такие части речи, как существительное (мужского, женского, среднего рода), прилагательное, глагол, наречие, союз, числительное, частица, междометие, местоимение, предлог. Можно выбрать как одну часть речи из списка, так и несколько.
Далее представлен поиск по дате. Существует возможность поиска по точному году, а также по диапазону. Кроме того, можно искать по веку. Для этого нужно выбрать нужный век из списка (можно выбрать как один век, так и несколько).  Кроме того, существует поиск по дате первого упоминания. Он устроен так же, как и поиск по дате.
Далее следует поиск по словарю с учетом информации из списка источников. Доступен поиск по языку оригинала источника. Есть возможность поиска только переводных или только непереводимых источников. Кроме того, есть возможность выбрать язык оригинала источника. На данный момент в таблице со списком источников представлены такие языки, как греческий, латынь, немецкий, польский и чешский.
Также существует поиск по жанру источника. В классификации из списка источников приведены следующие жанры: Библия и апокрифы, богословие, гомилетика, агиография, повести и беллетристика, литургика, эпистолография, летопись, хроника и хронография, документы.
####Поиск по списку источников
Также существует отдельный поиск по списку источников. В нем представлены следующий функции: поиск по названию источника, поиск по языку оригинала, поиск по жанру источника, поиск по году создания списка и поиск по году создания текста. В поле «поиск по названию» производится поиск по полному названию источника. Поиск по языку оригинала, дате и жанру устроен так же, как в поиске по словарю с учетом информации из списка источников.
####Выдача результата
На странице с результатами отображается список заголовочных форм словарных статей, которые подходят по параметрам, введенным пользователем. Для того, чтобы открыть всю словарную статью, нужно кликнуть на нужную заголовочную форму. 
Статья на странице выдачи выглядит так же, как статья в словаре. За заголовочной формой следует грамматические пометы, определение и зона примеров. Кликнув на грамматическую помету, то откроется новая страница выдачи со списком слов, которые содержат такую же грамматическую помету. Например, если кликнуть на помету «м» в приведенном ниже примере, то откроется страница со списком всех существительных мужского рода.

Также в случае, если в словарной статье присутствует ссылка на другую статью, если кликнуть на слово, на которое ссылается статья, то откроется новая страница поиска, на которой будет отображаться словарная статья, к которой относилась ссылка.
При поиске по списку источников на странице выдачи результатов отображается список названий источников, которые подходят по параметрам, указанным пользователем.
##Результаты
Была создана электронная база данных на основе Словаря русского языка XI–XVII вв. Также был создан интерфейс для поиска по словарю. Поиск по словарю объединен с поиском по списку источников, который делает возможным поиск по словарю с учетом информации, представленной в таблице с информацией об источниках. Также был создан отдельный интерфейс для поиска по источникам. Электронная версия словаря доступна по ссылке: http://web-corpora.net/wsgi/oldrus.wsgi/dict. Все исходные файлы и скрипты, использующиеся для работы программы, доступны на GitHub по ссылке: https://github.com/AnnaVechkaeva/RusDict/tree/master/DB 