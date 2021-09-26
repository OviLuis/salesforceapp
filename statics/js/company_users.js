$(document).ready(
    init
)


function init(){
    var company_id = $('#id_company').val();
    console.log(company_id)
    if (company_id){
        load_users_by_company(company_id);
    }



}


//Invitar usuario
$('#invite-user-form').on('click', function(){

    var url = 'http://localhost:8000/api/v1/companyUsers/'

    var form_data = {
        "status": "S",
        "id_company": $('#id_company').val(),
        "id_user": $('#id_users').val()
    }

    $.ajax({
        type: 'POST',
        url: url,
        dataType: "json",
        contentType: 'application/x-www-form-urlencoded; charset=utf-8',
        data: form_data,
        processData: true,
        success: function(data){
            //$(".overlay-example").hide();
            console.log()
            console.log(data.status)


        },
        error: function(xhr){
            console.log(xhr);
            if(xhr.responseJSON){
                var err_msg = ''
                $.each(xhr.responseJSON, function(k,v){
                    err_msg += v[0]+'\n';
                })

                alert(err_msg);
            }
        },
    }); //ajax
})


//obtener usuario invitados a una empresa propietaria
function load_users_by_company(company_id){
    var url = 'http://localhost:8000/api/v1/users-by-company/'+company_id;
    console.log('url............')
    console.log(url)
    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",
        contentType: 'application/x-www-form-urlencoded; charset=utf-8',
        processData: true,
        success: function(data){
            //$(".overlay-example").hide();
            console.log(data)
            var item = '';
            $.each(data, function(k, v){
                item = '<tr>'
                item += '<td>'+v.id+'</td>';
                item += '<td>'+v.user_name +'</td>';
                item += '<td>'+v.comp_name +'</td>';
                item += '<td>'+v.las_login +'</td>';
                item += '<td>'+v.status +'</td>';
                item += '<td><button type="button" class="remove_user_by_company" data-user_company="'+v.id +'">Eliminar</button></td>';
                item += '</tr>'


            })
            $(document).find('#companies-users-table tbody').html(item);

        },
        error: function(xhr){
            console.log(xhr);
        },
    }); //ajax
}


//Remover Usuario invitadod a Empresa propietaria
$('.remove_user_by_company').on('click', function(){
    console.log('remove_user_by_company..............')
    var user_company_id = $(this).data('user_company')
    console.log(user_company_id);

     url = 'http://localhost:8000/api/v1/companyUsers/'+user_company_id;
    $.ajax({
        type: 'DELETE',
        url: url,
        dataType: "json",
        contentType: 'application/x-www-form-urlencoded; charset=utf-8',
        data: form_data,
        processData: true,
        success: function(data){
            //$(".overlay-example").hide();
            console.log(data.status)


        },
        error: function(xhr){
            console.log(xhr);
            if(xhr.responseJSON){
                var err_msg = ''
                $.each(xhr.responseJSON, function(k,v){
                    err_msg += v[0]+'\n';
                })

                alert(err_msg);
            }
        },
    }); //ajax


})