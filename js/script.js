const loctn = 'http://127.0.0.1:5500/devlpr-3nity/devlpr-3nity';

function rate(e, star) {
    let t = $('.totalBL').text();
    if (e.classList.contains("fa-star-o") == true) {
        e.classList.remove("fa-star-o");
        e.classList.add("fa-star");
        let res = Math.round(t) + 1;
        $('.totalBL').text(res)
    }else{
        e.classList.remove("fa-star");
        e.classList.add("fa-star-o");
        let res = Math.round(t) - 11;
        $('.totalBL').text(res);
    }
}
function likeAuthor(authorId) {
    let t = Math.round($('#totalL').text());
    let res = t + 1;
    $('#totalL').text(res);
}
function followAuthor(authorId) {
    let t = Math.round($('#totalF').text());
    let res = t + 1;
    $('#totalF').text(res);
}

function sharePost(id, title, author, date) {
    $('#share-blog-title').text(title);
    $('#share-blog-author').text(author);
    $('#share-blog-date').text(date);

    let shareTo = '';
    shareTo += `<span><a href=""><i class="fa fa-facebook-square" aria-hidden="true"></i></a></span>`;
    shareTo += `<span><a href=""><i class="fa fa-whatsapp" aria-hidden="true"></i></a></span>`;
    shareTo += `<span><a href=""><i class="fa fa-instagram" aria-hidden="true"></i></a></span>`;
    shareTo += `<span><a href=""><i class="fa fa-twitter-square" aria-hidden="true"></i></a></span>`;
    $('#share-to').html(shareTo);

    $('#share-modal').show();
}

function cloSe(id) {
    $('#'+id).hide();
}

var getParams = function (url) {
	var params = {};
	var parser = document.createElement('a');
	parser.href = url;
	var query = parser.search.substring(1);
	var vars = query.split('&');
	for (var i = 0; i < vars.length; i++) {
		var pair = vars[i].split('=');
		params[pair[0]] = decodeURIComponent(pair[1]);
	}
	return params;
};

function reaD(name){
    $('body').load(`${loctn}/posts/${name}.txt`)
    // $.get(`posts/${name}.txt`, {}, function (content) {
    //     let lines = content.split('\n');
    //     console.log(`"${name}.txt" contains ${lines.length} lines`)
    //     console.log(`First line : ${lines[0]}`)
    // })
    // const fs = require('fs');
    // fs.readFile(`${loctn}/posts/${name}.txt`, 'utf-8', (err, data) => {
    //     if (err) throw err;
    //     console.log(data);
    // })
    var txtFile = new XMLHttpRequest();
    txtFile.open("GET", `${loctn}/posts/${name}.txt`, true);
    // console.log(txtFile);
    txtFile.onreadystatechange = function(){
        console.log(txtFile.responseText);
        if (txtFile.readyState === 4) {
            if (txtFile.status === 200) {
                console.log(txtFile.responseText);
                $('#postBody').html(txtFile.responseText);
            }
        }
    }
}

window.addEventListener('DOMContentLoaded', function () {
    if ((window.location.href).includes('post')) {
        let q = (getParams(window.location.href)).post;
        console.log(q)
        reaD(q);
    }else{
        window.location=window.location.href+'?post=1';
    }
})