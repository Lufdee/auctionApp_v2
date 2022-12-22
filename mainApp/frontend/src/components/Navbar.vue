<template>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              
                <li class="nav-item">
                    <router-link to="/" class="nav-link">Home</router-link>
                </li>
                <li class="nav-item">
                    <router-link to="/profile" class="nav-link">Profile</router-link>
                </li>
            </ul>
            
            <ul class="navbar-nav">
            <a class = "btn btn-outline-success" type="button"
                href="http://localhost:8000/api/logout/">Logout</a>
            <a class="btn btn-outline-success" type ="button" href="http://localhost:8000/api/login/">Login</a>
            </ul>
        </div>
    </div>
</nav>

</template>

<script>
    export default {
        data() {
            return {
                loggedIn: '',
            }
        },
        methods:{
        }
    }
</script>