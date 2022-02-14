function delete_job(job_id){
    Swal.fire({
        icon: 'warning',
        title: 'Warning',
        text:'Are you sure you want to delete this job in your list?',
        showCancelButton: true,
        confirmButtonText: 'Delete',
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          Swal.fire('','','success')
          window.location.href = "../delete_job/" +"?job_id=" + job_id
        } else if (result.isDenied) {
          Swal.fire('Changes are not saved', '', 'info')
        }
      })
}