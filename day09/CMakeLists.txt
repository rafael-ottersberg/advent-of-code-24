add_library( day09 day09.cpp)

target_include_directories(day09 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day09 TBB::tbb )