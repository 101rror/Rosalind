
<h2><a href="https://rosalind.info/problems/ba1b/">Find the Most Frequent Words in a String</a></h2>

<p>We say that Pattern is a <strong>most frequent k-mer</strong> in Text if it maximizes Count(Text, Pattern) among all <a href="https://rosalind.info/glossary/k-mer/">k-mers</a> . For example, "ACTAT" is a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT", and "ATA" is a most frequent 3-mer of "CGATATATCCATAG".</p>

<p><strong class="example">Frequent Words Problem</strong></p>
<p>Find the most frequent k-mers in a string.</p>

<p><strong>Given : </strong> A <a href="https://rosalind.info/glossary/dna-string/">DNA string</a> Text and an integer k.</p>
<p><strong>Return : </strong> All most frequent k-mers in Text (in any order).</p>



<p>&nbsp;</p>
<p><strong class="example">Sample Dataset</strong></p>
<pre>
<strong>ACGTTGCATGTCGCATGATGCATGAGAGCT</strong>
<strong>4</strong>
</pre>
<p><strong class="example">Sample Output</strong></p>
<pre>
<strong>CATG GCAT</strong>
</pre>
