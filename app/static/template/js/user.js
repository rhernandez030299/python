$(document).ready(function(){
    //Función para validar los datos antes de enviarlos
    $("#formulario-usuario").validate({

        submitHandler: function(form){
            var data = {};

            data.username = $("#username").val().trim();
            data.email = $("#email").val().trim();
            data.password = $("#password").val().trim();
            data.csrf_token = $("#csrf_token").val().trim();
            
            ajax('user/insert',data,function(response){
            
                heading = "Ingresado!";
                text = response.msg;
                icon = "info";
                res = "info";

                if(response.res == 0){
                    heading = "Alerta";
                    icon = "error";
                    res = "danger";
                }

                $("#username, #email, #password").val("");

                return md.showNotification('top','right', res, text, icon);
            });
        }
    });


    
    /*$('#user-table').DataTable({
        
        "lengthMenu": [
        [10, 25, 50, -1],
        [10, 25, 50, "All"]
        ],
        responsive: true,
        language: {
            search: "_INPUT_",
            searchPlaceholder: "Search records",
        }
    });*/

    //Creacion de la tabla canales
    var dataTable_user = $('#user-table').DataTable({
        "processing":true,
        "serverSide":true,
        "responsive": true,
        "pagingType": "full_numbers",
        "order":[],

        "ajax":{
            url: base_url+"user/user_list",
            type:"POST"
        },
        "columnDefs":[
        {
            "targets":[1],
            "orderable":false,
        },
        ],
        "rowCallback": function( row, data ) {

        }
    });

});