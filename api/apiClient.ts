import axios, { AxiosRequestConfig } from 'axios';

// Define the response structure for GET requests
export interface FetchResponse<T> {
  count: number;
  next: string | null;
  results: T[];
}

// Define the response structure for POST and PUT requests
export interface PostPutResponse<T> {
  data: T;
}

// Create an instance of Axios with a base URL and default query parameters
const axiosInstance = axios.create({
  baseURL: 'your api base url',
  params: {
    key: ' your api-key to access',
  },
});

class APIClient<T> {
  endPoint: string;

  constructor(endPoint: string) {
    this.endPoint = endPoint;
  }

  // Generic method for making GET requests
  getData = (config: AxiosRequestConfig = {}): Promise<FetchResponse<T>> => {
    return axiosInstance
      .get<FetchResponse<T>>(this.endPoint, config)
      .then((res) => res.data);
  };

  // Generic method for making POST requests
  postData = (data: T): Promise<PostPutResponse<T>> => {
    return axiosInstance
      .post<PostPutResponse<T>>(this.endPoint, data)
      .then((res) => res.data);
  };

  // Generic method for making PUT requests
  putData = (
    data: T,
    config: AxiosRequestConfig = {}
  ): Promise<PostPutResponse<T>> => {
    return axiosInstance
      .put<PostPutResponse<T>>(this.endPoint, data, config)
      .then((res) => res.data);
  };

  // Generic method for making DELETE requests
  deleteData = (config: AxiosRequestConfig = {}): Promise<void> => {
    return axiosInstance.delete(this.endPoint, config).then(() => {
      // Assuming that DELETE request does not return any data
    });
  };
}

export default APIClient;
