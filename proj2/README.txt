The following transformations bring the point clouds in this directory in close proximity wrt each other. After the transformation you can run ICP on them.



#ifdef GH17_GH23
//gh17.ptx -> gh23.ptx

//3x3 matrix of first 3 columns, rows: rotation
//last column: translation
static double M[] = {
      0.769006,  0.300208,  0.564362,  15.474807,
     -0.340899,  0.939441, -0.035215, - 2.941283,
     -0.540756, -0.165310,  0.824776, - 4.791782
};
#else
// gh17.ptx -> gh16.ptx

//3x3 matrix of first 3 columns, rows: rotation
//last column: translation
static double M[] = {
      0.999953, 0.004953,  0.008324, -0.000003,
     -0.003077, 0.977294, -0.211865,  0.001217,
     -0.009184, 0.211829,  0.977264,  0.017408
};
#endif
