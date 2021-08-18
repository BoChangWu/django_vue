<template>
    <div id="login">
        <h1>login</h1>
        <h1>{{usr}}</h1>
        <LoginForm/>
    </div>
</template>

<script>
import axios from 'axios'
import LoginForm from '@/components/LoginForm.vue'
export default {
    name: 'Login',
    data(){
        return{
            usr: '',
        }
    },
    methods:{
        getUsr(){
            const path = 'http://localhost:8000/shoppin/login'
            axios.get(path)
                .then((res) => {
                    this.usr = res.data
                    console.log(res.data)
                })
                .catch((error) => {
                    console.log(error)
                })
        }
    },
    created(){
        this.getUsr()
    },
    components:{
        LoginForm,
    }
}
</script>
<style>

</style>