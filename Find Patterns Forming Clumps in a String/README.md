<h2><a href="https://rosalind.info/problems/ba1e/">Find Patterns Forming Clumps in a String</a></h2>

<p>&nbsp;</p>
<p><strong class="example"></strong></p>

<p>Given integers <strong><i>L</i></strong> and <strong><i>t</i></strong>, a <a href="https://rosalind.info/glossary/string/">string</a> <i>Pattern</i> forms an <strong><i>(L, t)</i>-clump</strong> inside a (larger) <a href="https://rosalind.info/glossary/string/">string</a> <i>Genome</i> if there is an interval of <i>Genome</i> of length <strong><i>L</i></strong> in which <i>Pattern</i> appears at least <strong><i>t</i></strong> times.</p>
<p>For example, <strong>TGCA</strong>  forms a (25,3)-clump in the following Genome:   gatcagcataagggtccc<strong><i>TGCA</i></strong>A<strong><i>TGCA</i></strong>TGACAAGCC<strong><i>TGCA</i></strong>gttgttttac.</p>

<p><strong class="example">Clump Finding Problem</strong></p>
<p><i>Find patterns forming clumps in a string</i>.</p>

<ol>
<p><strong>Given : </strong> A string <i>Genome,</i> and integers <strong><i>k</i></strong>, <strong><i>L</i></strong>, and <strong><i>t</i></strong>.</p>
<p><strong>Return : </strong> All distinct <i>k</i>-mers forming <strong><i>(L, t)</i></strong>-clumps in <i>Genome</i>.</p>
</ol>


<p>&nbsp;</p>
<p><strong class="example">Sample Dataset</strong></p>
<pre>
<strong>CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC</strong>
<strong>5 75 4</strong>
</pre>
<p><strong class="example">Sample Output</strong></p>
<pre>
<strong>CGACA GAAGA AATGT</strong>
</pre>
