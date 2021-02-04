<template>
    <div>
        <div v-bind:key="user[0]" v-for="user in pendingList">
            <pendingItemList v-bind:pendingUser="user" v-on:del-user="$emit('del-user',user[0])" v-on:approve-user="$emit('approve-user',user[0])"/>
        </div>
    </div>
</template>

<script>
import pendingItemList from '../components/pendingItem';
export default {
  name: "Pending",
  components:{
      pendingItemList
  },
  props: ['pendingList']
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
