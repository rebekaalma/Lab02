$(document).ready(function () {

    $.get('/todolist/json', function (data) {
    data.map((singleData) =>
        $('#card-body').append(`<div class="col">
       <div class="card" style="width: 18rem;">
         <div class="card-body">
 
           <h5 class="card-title">${singleData.fields.user}</h5>
           <h6 class="card-subtitle mb-2 text-muted">${singleData.fields.date}</h6>
           <h6 class="card-subtitle mb-2 text-muted"${singleData.fields.title}</h6>
           <h6 class="card-subtitle mb-2 text-muted">${singleData.fields.is_finished}</h6>
           <p class="card-text">${singleData.fields.description}</p>
           <a href="/todolist/marker/${singleData.pk}   " class="card-link"><button>Update</button></a>
           <a href="/todolist/delete/${singleData.pk}" class="card-link"><button>Delete</button></a>
         </div>
       </div>
     </div>`)
    );
    });
});