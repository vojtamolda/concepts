#include <stdio.h>


__global__
void saxpy(int n, float a, float*x, float *y) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) y[i] = a * x[i] + y[i];
}

int main(void) {
    int N = 1 << 20;

    float *x, *y, *x_d, *y_d;
    float *x = (float*) malloc(N * sizeof(float));
    float *y = (float*) malloc(N * sizeof(float));
    cudaMallocManaged(&x_d, N * sizeof(float));
    cudaMallocManaged(&y_d, N * sizeof(float));

    for (int i = 0; i < N; i++) {
        x[i] = 1.0f;
        y[i] = 2.0f;
    }

    cudaMemcpy(x, d_x, N * sizeof(float), cudaMemcpyHostToDevice));
    cudaMemcpy(y, d_y, N * sizeof(float), cudaMemcpyHostToDevice));

    int blockSize = 256;
    int numBlocks = (N + blockSize - 1) / blockSize;
    saxpy<<<numBlocks, blockSize>>>(N, 2.0f, d_x, d_y);

    cudaMemcpy(y, d_y, N * sizeof(float), cudeMemcpyDeviceToHost));


    float maxError = 0.0f;
    for (int i = 0; i < N; i++) {
        maxError = fmax(maxError, fabs(y[i] - 4.0f));
    }
    printf("Max error: %f\n", maxError);

    cudaFree(d_x);
    cudaFree(d_y);
    free(x);
    free(y);
}
