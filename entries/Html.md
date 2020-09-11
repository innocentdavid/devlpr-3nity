### In this Article you'll learn: 
* Meaning of HTML
* Basic Html Tags
* Create your first Website

## What is HTML?
Html is a Markup Language which stands for Hypertext Markup Language. am not really going to go into the history for now we are just going to learn how to use it in Web Development.

## Html Structure
Below is the structure of a Web page:

`<!doctype html>`  
`<html>`  
`<head></head>`  
`<body></body>`  
`</html>`  
The `<head>` Tag do contain the none visible contents that is the contents are not going to show up in the web page,
But the `<body>` Tag do contain the visible contents of your web page.
Information like `<title>` of a webpage, `<meta>` for description and also to specify **viewport**, **links**, **scripts**... etc are put in the `<head>` Tag.

## Html Elements
Html Elements are divided into two:

* Block Level Element and
* Inline Level Element
  
##### Block Level Element
Block Level Element are those element which at default take up the whole row and they do start from new line
Examples are: The `<h>s`, `<div>`, `<br>`, `<hr>`... etc

##### Inline Level Element
Inline Level Element are those element which at default do not take up the whole row and they can continue where another stops
Examples are: the `<small>`, `<span>`, `<b>`, `<i>`... etc

Note: when writing **Elements** it do have **Opeing tag <>** and **Closing tag </>** e.g. `<div> Content will be here </div>` though not all Elements requeire closing tag e.g. `<img />, <br />`...etc

There are a lot of html elements but am going to explain some of them which you'll need the most for now because you can't learn them all at once.

### `<h1> - <h6>`

The headers - Starting from **h1** which is the biggest to **h6** the smallest
<h1 style="display:inline-block;">Heading 1</h1> - `<H1>`

<h2 style="display:inline-block;">Heading 2</h2> - `<H2>`

<h3 style="display:inline-block;">Heading 3</h3> - `<H3>`

<h4 style="display:inline-block;">Heading 4</h4> - `<H4>`

<h5 style="display:inline-block;">Heading 5</h5> - `<H5>`

<h6 style="display:inline-block;">Heading 6</h6> - `<H6>`


### `<ol> & <ul>`
**ol** Stands for ordered list while **ul** stands for unordered list
Example of ordered list:  
`<ol>`  
`<li>`List 1`</li>`  
`<li>`List 2`</li>`  
`</ol>`  
will result:
<ol>
<li>List 1</li>
<li>List 2</li>
</ol>

Example of unordered list:  
`<ul>`  
`<li>`List 1`</li>`  
`<li>`List 2`</li>`  
`</ul>`  
will result:
<ul>
<li>List 1</li>
<li>List 2</li>
</ul>