from typing import Tuple

import numpy as np
from pyrr import Matrix44


class Projection:
    """"""
    def __init__(self, aspect_ratio=9 / 16, fov=75, near=1, far=100):
        """
        Create a projection

        Keyword Args:
            aspect_ratio (float): Sspect ratio
            fov (float): Field of view
            near (float): Near plane value
            far (float): Far plane value
        """
        self._aspect_ratio = aspect_ratio
        self._fov = fov
        self._near = near
        self._far = far
        self._matrix = None
        self._matrix_bytes = None
        self.update()

    @property
    def fov(self, value) -> float:
        """Current field of view"""
        return self._far
    
    @property
    def near(self) -> float:
        """Current near plane value"""
        return self._near
    
    @property
    def far(self) -> float:
        """Current far plane value"""
        return self._far

    @property
    def matrix(self) -> np.ndarray:
        """Current numpy projection matrix"""
        return self._matrix

    def update(self, aspect_ratio=None, fov=None, near=None, far=None) -> None:
        """
        Update the projection matrix

        Keyword Args:
            aspect_ratio (float): Sspect ratio
            fov (float): Field of view
            near (float): Near plane value
            far (float): Far plane value
        """
        self._aspect_ratio = aspect_ratio or self._aspect_ratio
        self._fov = fov or self._fov
        self._near = near or self._near
        self._far = far or self._far

        self._matrix = Matrix44.perspective_projection(self._fov, self._aspect_ratio, self._near, self._far)
        self._matrix_bytes = self._matrix.astype('f4').tobytes()

    def tobytes(self) -> bytes:
        """
        Get the byte representation of the projection matrix
        """
        return self._matrix_bytes

    @property
    def projection_constants(self) -> Tuple[float, float]:
        """
        (x, y) projection constants for the current projection.
        This is for example useful when reconstructing a view position
        of a fragment from a linearized depth value.
        """
        return self._far / (self._far - self._near), (self._far * self._near) / (self._near - self._far)