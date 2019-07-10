"""Shader Registry"""
from moderngl_window.resources.base import BaseRegistry
from moderngl_window.resources.meta import ProgramDescription


class Programs(BaseRegistry):
    """
    A registry for shaders requested by effects.
    Once all effects are initialized, we ask this class to load the shaders.
    """
    settings_attr = 'PROGRAM_LOADERS'

    def resolve_loader(self, meta: ProgramDescription):
        """Resolve program loader"""
        if not meta.kind:
            meta.kind = 'single' if meta.path else 'separate'

        return super().resolve_loader(meta)


programs = Programs()
