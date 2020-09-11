window.addEventListener('DOMContentLoaded', () => {
    status();
})
function status(go, dest) {
    fetch('/', {
        method: 'POST',
        body: JSON.stringify({action:'status'})
    })
    .then(res => res.json())
    .then(res => {
        $('#status')[0].value = res.user;
        if (res.user == 'AnonymousUser') {
            if (go == 'yes') {
                window.location = `/login?next=${dest}`;
            }else{
                // console.log($('#llr'));
                // alert('You are not logged in');
            }
        }
    })
}

function rate(postId) {
    let t = $('.totalBL').text();
    let e = $('.rateStarBtn')[0];
    console.log(e);
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

function entryListLi(entry) {
    window.location= '/blog/'+entry.toLowerCase()
}

function searchPost() {

}

function authorSearch() {
    let author = $('#authorSearcInp')[0].value;
    window.location='/author/'+author;
}

function commentCount() {
    let postId = $('#postId')[0].value;
    fetch('/comment', {
        method:'POST',
        body:JSON.stringify({action:'count', body:'', postId:postId})
    })
    .then(res => res.json())
    .then(res => {
        // console.log(res);
        $('#commentCount').text(res.commentCount);
    })    
}

function comment(postId) {
    let loading = `<img src="/static/blog/images/loading2.gif" style="width: 50px; height: 30px;"
    alt="loading">`;
    let comment = $('#commentField')[0].value;
    let visitor = $('#vname')[0].value;
    $('.commentLloading').html(loading);

    fetch('/comment', {
        method: 'POST',
        body:JSON.stringify({action:'comment', body:comment, visitor:visitor, postId:postId})
    })
    .then(res => res.json())
    .then(res => {
        $('.commentLloading').html('');
        if (res.message == 'ok') {
            $('#commentField')[0].value = '';
            window.location= '#commentz';
            location.reload();
        }else{
            alert(res.message + ' occured! Please Try Again');
        }
    })
}

function composeForm() {
    // let data = $('#composeForm').serialize();
    let fn = $('#composeForm-fname')[0].value;
    let t = $('#composeForm-title')[0].value;
    if (fn == ''){alert("Author's name cannot be empty")}else{
        if (t == ''){alert("Author's name cannot be empty")}else{
            fetch ('createPost', {
                method: 'POST',
                body: JSON.stringify({
                    fname:fn, title:t,
                    tags:$('#composeForm-tags')[0].value,
                    fVideo:$('#composeForm-fVideo')[0].value,
                    content:$('#composeForm-content')[0].value,
                }),
            })
            .then(res => res.json())
            .then(data => {
                // console.log(data);
                if(data.message == 'ok'){
                    $('#composeForm')[0].reset();
                    window.location = '/blog/'+t.toLowerCase();
                }else{
                    alert(data.message);
                }
            })
        }
    }
}