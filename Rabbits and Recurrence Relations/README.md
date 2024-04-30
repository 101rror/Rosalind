<h2><a href="https://rosalind.info/problems/fib/">Rabbits and Recurrence Relations</a></h2>

<p>&nbsp;</p>
<p><strong class="example">Problem</strong></p>


<p>A <a href="https://rosalind.info/glossary/sequence/">sequence</a> is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite or infinite. Two examples are the finite sequence <i>(π,−2–√,0,π)</i> and the infinite sequence of odd numbers <strong>(1,3,5,7,9,…)</strong>. We use the notation <i>a<sub>n</sub></i> to represent the <i>n</i>-th term of a sequence.</p>
 
<p>A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior. As a result, if <strong><i>F<sub>n</sub></i></strong> represents the number of rabbit pairs alive after the <i>n</i>-th month, then we obtain the <a href="https://rosalind.info/glossary/fibonacci-sequence/">Fibonacci sequence</a> having terms <strong><i>F<sub>n</sub></i></strong> that are defined by the recurrence relation <strong><i>F<sub>n</sub> = F<sub>n−1</sub> + F<sub>n-2</sub></i></strong> (with <strong><i>F<sub>1</sub> = F<sub>2</sub> = 1</i></strong> to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.</p>

<p>When finding the <i>n</i>-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of <i>n</i>. This problem introduces us to the computational technique of <a href="https://rosalind.info/glossary/dynamic-programming/">dynamic programming</a>, which successively builds up solutions by using the answers to smaller cases.</p>

<p><strong>Given : </strong>A DNA string s of length at most 1000 <a href="https://rosalind.info/glossary/base-pair/">bp</a>.</p>
<p><strong>Return : </strong>The reverse complement s<sup>c</sup> of s.</p>



<p>&nbsp;</p>
<p><strong class="example">Sample Dataset</strong></p>
<pre>
<strong>AAAACCCGGT</strong>
</pre>
<p><strong class="example">Sample Output</strong></p>
<pre>
<strong>ACCGGGTTTT</strong>
</pre>
