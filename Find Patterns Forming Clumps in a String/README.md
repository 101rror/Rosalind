<h2><a href="https://rosalind.info/problems/ba1e/">Find Patterns Forming Clumps in a String</a></h2>

<p>&nbsp;</p>
<p><strong class="example"></strong></p>

<p>Given integers L and <i>t</i>, a <a href="https://rosalind.info/glossary/string/">string</a> <i>Pattern</i> forms an <strong><i>(L, t)</i>-clump</strong> inside a (larger) <a href="https://rosalind.info/glossary/string/">string</a> <i>Genome</i> if there is an interval of <i>Genome</i> of length L in which <i>Pattern</i> appears at least <i>t</i> times.</p>
<p>For example, <strong>TGCA</strong>  forms a (25,3)-clump in the following Genome:   gatcagcataagggtccc<strong><i>TGCA</i></strong>A<strong><i>TGCA</i></strong>TGACAAGCC<strong><i>TGCA</i></strong>gttgttttac.</p>

<p><strong class="example">Clump Finding Problem</strong></p>
<p>Find patterns forming clumps in a string.</p>

<p><strong>Given : </strong> A string Genome, and integers k, L, and t.</p>
<p><strong>Return : </strong> All distinct k-mers forming (L, t)-clumps in Genome.</p>



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
