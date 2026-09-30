use pyo3::prelude::*;

/// Cellcast_python's parent module.
#[pymodule(name = "cellcast")]
mod cellcast_module {
    #[pymodule_export]
    use super::models;
}

#[pymodule]
mod models {
    #[pymodule_export]
    use crate::classes::stardist_classes::PyStarDist2D;
    #[pymodule_export]
    use crate::classes::stardist_classes::PyStarDist3D;
}