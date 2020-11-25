<p class="has-line-data" data-line-start="0" data-line-end="1">There are a few Files that are Important for a package to be publishable to Pypi</p>
<ol>
<li class="has-line-data" data-line-start="2" data-line-end="3"><a href="http://setup.py">setup.py</a> (check the code)</li>
<li class="has-line-data" data-line-start="3" data-line-end="4">setup.cfg (check the code)</li>
<li class="has-line-data" data-line-start="4" data-line-end="5">LICENSE.txt (<a href="https://opensource.org/licenses/">https://opensource.org/licenses/</a>) To get open Sourse LICENSE</li>
<li class="has-line-data" data-line-start="5" data-line-end="7"><a href="http://README.md">README.md</a> (<a href="https://dillinger.io/">https://dillinger.io/</a>) To make Beautiful <a href="http://README.md">README.md</a></li>
</ol>
<p class="has-line-data" data-line-start="7" data-line-end="8">When all of the above files are ready</p>
<p class="has-line-data" data-line-start="9" data-line-end="10">The Final Step is :-</p>
<ul>
<li class="has-line-data" data-line-start="11" data-line-end="12">python <a href="http://setup.py">setup.py</a> sdist bdist_wheel</li>
<li class="has-line-data" data-line-start="12" data-line-end="13">twine upload dist/*</li>
</ul>
