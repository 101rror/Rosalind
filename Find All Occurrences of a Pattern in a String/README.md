<h2><a href="https://rosalind.info/problems/ba1d/">Find All Occurrences of a Pattern in a String</a></h2>

<p>&nbsp;</p>
<p><strong class="example"></strong></p>

<p>In this problem, we ask a simple question: how many times can one <a href="https://rosalind.info/glossary/string/">string</a> occur as a <a href="https://rosalind.info/glossary/substring/">substring</a> of another? Recall from <a href="https://rosalind.info/problems/ba1b/">“Find the Most Frequent Words in a String”</a> that different occurrences of a substring can overlap with each other. For example, <strong><i>ATA</i></strong> occurs three times in CG<strong><i>ATATA</i></strong>TCC<strong><i>ATA</i></strong>G.</p>

<p><strong class="example">Pattern Matching Problem</strong></p>
<p><i>Find all occurrences of a pattern in a string.</i></p>

<ol>
<p><strong>Given : </strong> Strings <i>Pattern</i> and <i>Genome</i>.</p>
<p><strong>Return : </strong> All starting positions in <i>Genome</i> where <i>Pattern</i> appears as a substring. Use <a href="https://rosalind.info/glossary/0-based-numbering/">0-based indexing.</a></p>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Sample Dataset</strong></p>
<pre>
<strong>ATAT</strong>
<strong>GATATATGCATATACTT</strong>
</pre>
<p><strong class="example">Sample Output</strong></p>
<pre>
<strong>1 3 9</strong>
</pre>
