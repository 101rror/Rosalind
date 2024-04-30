<h2><a href="https://rosalind.info/problems/ba1b/">Find the Most Frequent Words in a String</a></h2>

<p>&nbsp;</p>
<p><strong class="example"></strong></p>

<p>We say that <i>Pattern</i> is a <strong>most frequent <i>k</i>-mer</strong> in <i>Text</i> if it maximizes <i>Count(Text, Pattern)</i> among all <a href="https://rosalind.info/glossary/k-mer/">k-mers</a> . For example, "ACTAT" is a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT", and "ATA" is a most frequent 3-mer of "CGATATATCCATAG".</p>

<p><strong class="example">Frequent Words Problem</strong></p>
<p><i>Find</i> the most <i>frequent k-mers in a string</i>.</p>

<ol>
<p><strong>Given : </strong> A <a href="https://rosalind.info/glossary/dna-string/">DNA string</a> <strong><i>Text</i></strong> and an integer <strong><i>k</i></strong>.</p>
<p><strong>Return : </strong> All most frequent <i>k</i>-mers in <i>Text</i> (in any order).</p>
</ol>


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
