function delete_job_seeker(user_id){
    Swal.fire({
        icon: 'warning',
        title: 'Warning',
        text:'Are you sure you want to delete this job seeker in your list?',
        showCancelButton: true,
        confirmButtonText: 'Delete',
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          Swal.fire('','','success')
          window.location.href = "../delete_user/" +"?user_id=" + user_id
        } else if (result.isDenied) {
          Swal.fire('Changes are not saved', '', 'info')
        }
      })
}