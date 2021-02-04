<template>
    <div>
        <div v-bind:key="user[0]" v-for="user in usersList">
            <userItemList v-bind:user="user" v-on:del-user="$emit('del-user',user[0])"/>
        </div>
    </div>
</template>

<script>
import userItemList from '../components/userItem';
export default {
  name: "Users",
  components:{
      userItemList
  },
  props: ['usersList']
}
</script>

<style scoped>
  .user-item {
    background: #f4f4f4;
    padding: 10px;
    border-bottom: 1px #ccc dotted;
  }

  .is-complete {
    text-decoration: line-through;
  }

  .del {
    background: #5f5f5f;
    color: #fff;
    border: none;
    padding: 5px 9px;
    border-radius: 50%;
    cursor: pointer;
    float: right;
  }
</style>
