add_library( day24 day24.cpp)

target_include_directories(day24 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day24 TBB::tbb )