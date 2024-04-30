<h2><a href="https://rosalind.info/problems/ba1c/">Find the Reverse Complement of a String</a></h2>

<p>&nbsp;</p>
<p><strong class="example"></strong></p>

<p>In <a href="https://rosalind.info/glossary/dna-string/">DNA strings</a>,  symbols 'A' and 'T' are <a href="https://rosalind.info/glossary/complementary-base/">complements</a> of each other, as are 'C' and 'G'. Given a <a href="https://rosalind.info/glossary/nucleotide/">nucleotide</a> p, we denote its complementary nucleotide as <i>p̅</i>. The <a href="https://rosalind.info/glossary/reverse-complement/"> reverse complement</a> of a DNA string <i>Pattern* = p<sub>1</sub>…p<sub>n</sub></i> is the string <i>Pattern = p̅<sub>n</sub>…p̅<sub>1</sub></i> formed by taking the complement of each nucleotide in <i>Pattern</i>, then reversing the resulting string. </p>
<p>For example, the reverse complement of <i>Pattern</i> = "GTCA" is <i>Pattern*</i> = "TGAC".</p>


<p><strong class="example">Reverse Complement Problem</strong></p>
<p><i>Find the reverse complement of a DNA string</i>.</p>

<ol>
<p><strong>Given : </strong> A <a href="https://rosalind.info/glossary/dna-string/">DNA string</a> <i>Pattern</i>.</p>
<p><strong>Return : </strong><i>Pattern*</i>, the reverse complement of <i>Pattern</i>.</p>
</ol>


<p>&nbsp;</p>
<p><strong class="example">Sample Dataset</strong></p>
<pre>
<strong>AAAACCCGGT</strong>
</pre>
<p><strong class="example">Sample Output</strong></p>
<pre>
<strong>ACCGGGTTTT</strong>
</pre>
