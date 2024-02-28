
<h2><a href="https://rosalind.info/problems/ba1d/">Find All Occurrences of a Pattern in a String</a></h2>

<p>In this problem, we ask a simple question: how many times can one <a href="https://rosalind.info/glossary/string/">string</a> occur as a <a href="https://rosalind.info/glossary/substring/">substring</a> of another? Recall from <a href="https://rosalind.info/problems/ba1b/">“Find the Most Frequent Words in a String”</a> that different occurrences of a substring can overlap with each other. For example, <strong>ATA</strong> occurs three times in <strong>CGATATATCCATAG.</strong></p>

<p><strong class="example">Pattern Matching Problem</strong></p>
<p>Find all occurrences of a pattern in a string.</p>

<p><strong>Given : </strong> Strings Pattern and Genome.</p>
<p><strong>Return : </strong> All starting positions in Genome where Pattern appears as a substring. Use <a href="https://rosalind.info/glossary/0-based-numbering/">0-based indexing.</a></p>



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
