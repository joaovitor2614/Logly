<script setup lang="ts">

import { getUserInfoByID } from '@/api/services/user'
import { useProfessorStore, useUserStore } from '@/stores';
import { computed } from 'vue';
import { reactive } from 'vue';
import { onBeforeMount } from 'vue';
interface Props {
  //axis: Plot.Axis;
  comment: App.Professor.Comment,
  professorID: string
}

const props = defineProps<Props>();
const commentAuthorInfo: Partial<App.User.Info> = reactive({
  name: '',
  image: ''
})

const setCommentAuthorUserInfo = async () => {
  const { data: authorUserInfo, hasErrors } = await getUserInfoByID(props.comment.user_id)
  if (!hasErrors) {
    commentAuthorInfo.name = authorUserInfo.name
    commentAuthorInfo.image = authorUserInfo.image
  }

}

const userStore = useUserStore();
const professorStore = useProfessorStore();
const isCurrentAuthedUserCommentAuth = computed(() => props.comment.user_id === userStore.userInfo._id)
const deleteComment = () => {
  if (isCurrentAuthedUserCommentAuth.value) {
    professorStore.deleteComment(props.professorID,props.comment._id)
  }
}

onBeforeMount(() => {
  setCommentAuthorUserInfo()
 
})

</script>

<template v-if="commentAuthorInfo.name">
  <v-list-item class="comment">
    <v-row class="d-flex align-center">
      <v-col cols="6">
        <v-avatar color="primary" class="avatar">
          <v-img :src="commentAuthorInfo.image"></v-img>
          {{ commentAuthorInfo.name.charAt(0) }}
        </v-avatar>
      </v-col>
      <v-col cols="6"  v-if="isCurrentAuthedUserCommentAuth">
            <v-btn
          icon
          @click="deleteComment"
          
          style="color: red"
        >
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </v-col>
     
    </v-row>
    

    <v-list-item-content>
      <v-list-item-title class="author">
        {{  commentAuthorInfo.name }}
      </v-list-item-title>
      <v-list-item-subtitle class="timestamp">
        {{ props.comment.create_time }}
      </v-list-item-subtitle>
      <v-list-item-text class="content">{{ props.comment.text }}</v-list-item-text>
    </v-list-item-content>
  </v-list-item>

  <v-divider></v-divider>
</template>

<style scoped>
.comment {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 8px;
  border-radius: 8px;
  transition: background 0.2s ease-in-out;
}

.comment:hover {
  background: rgba(0, 0, 0, 0.05);
}

.avatar {
  font-size: 14px;
  font-weight: bold;
  color: white;
}

.author {
  font-weight: bold;
  font-size: 14px;
  color: #333;
}

.timestamp {
  font-size: 12px;
  color: gray;
}

.content {
  font-size: 14px;
  color: #444;
}
</style>