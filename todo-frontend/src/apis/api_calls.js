import axios from 'axios';
import {resolve} from './resolve';
import {API_ADDRESSES} from "./addresses";

export const addTodos = async (label_obj) => {
    return await resolve(axios.post(API_ADDRESSES['create'], label_obj).then(res => res.data));
};

export const fetchAllTodos = async () => {
    return await resolve(axios.get(API_ADDRESSES['fetchAll']).then(res => res.data));
}

export const updateTodos = async (id, label_obj) => {
    return await resolve(axios.post(`${API_ADDRESSES['update']}${id}/`, label_obj).then(res => res.data));
}

export const deleteTodos = async (id) => {
    return await resolve(axios.delete(`${API_ADDRESSES['delete']}${id}/`).then(res => res.data));
};


